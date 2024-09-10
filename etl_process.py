import pandas as pd
import psycopg2

# Open a connection to the PostgreSQL database
def open_connection():
    return psycopg2.connect(
        host="localhost", 
        dbname="nyc_taxi_db", 
        user="airflow", 
        password="airflow", 
        port="5432"
    )

def etl_process():
    # Extract: Connect to PostgreSQL and extract data
    conn = open_connection()
    df = pd.read_sql("SELECT * FROM nyc_taxi_trips", conn)
    
    # Transform: Add trip duration in minutes
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])
    df['trip_duration_minutes'] = df['trip_duration'] / 60
    
    # Load: Insert transformed data back into a new PostgreSQL table
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS nyc_taxi_trips_transformed (
        id VARCHAR PRIMARY KEY,
        vendor_id VARCHAR(10),
        pickup_datetime TIMESTAMP,
        dropoff_datetime TIMESTAMP,
        passenger_count INT,
        pickup_longitude FLOAT,
        pickup_latitude FLOAT,
        dropoff_longitude FLOAT,
        dropoff_latitude FLOAT,
        store_and_fwd_flag VARCHAR(1),
        trip_duration_minutes FLOAT
    )
    ''')
    
    for _, row in df.iterrows():
        cur.execute('''
        INSERT INTO nyc_taxi_trips_transformed 
        (id, vendor_id, pickup_datetime, dropoff_datetime, passenger_count, pickup_longitude, pickup_latitude,
         dropoff_longitude, dropoff_latitude, store_and_fwd_flag, trip_duration_minutes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', 
        (row['id'], row['vendor_id'], row['pickup_datetime'], row['dropoff_datetime'], row['passenger_count'],
         row['pickup_longitude'], row['pickup_latitude'], row['dropoff_longitude'], row['dropoff_latitude'],
         row['store_and_fwd_flag'], row['trip_duration_minutes']))

    conn.commit()
    cur.close()
    conn.close()
    print("ETL process completed successfully!")

# Execute the ETL process
if __name__ == '__main__':
    etl_process()
