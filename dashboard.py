import pandas as pd
import psycopg2
from dash import Dash, dcc, html
import plotly.express as px

# Function to connect to PostgreSQL
def open_connection():
    return psycopg2.connect(
        host="localhost", 
        dbname="nyc_taxi_db", 
        user="airflow", 
        password="airflow", 
        port="5432"
    )

def create_dashboard():
    # Extract transformed data from PostgreSQL
    conn = open_connection()
    df = pd.read_sql("SELECT * FROM nyc_taxi_trips_transformed where trip_duration_minutes< 1000", conn)
    conn.close()
    
    # Initialize Dash app
    app = Dash(__name__)
    
    # Create the layout of the dashboard
    app.layout = html.Div([
        html.H1("NYC Taxi Trips Dashboard"),
        html.Div("This dashboard displays NYC taxi trip statistics."),
        dcc.Graph(
            id='trip-duration-graph',
            figure=px.line(df, x='pickup_datetime', y='trip_duration_minutes', title='Trip Duration Over Time')
        )
    ])
    
    # Run the dashboard
    app.run_server(debug=True, use_reloader=False, port=8050)

# Execute the dashboard creation
if __name__ == '__main__':
    create_dashboard()
