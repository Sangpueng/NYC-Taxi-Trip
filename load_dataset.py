import pandas as pd
import psycopg2

# Load the dataset
df = pd.read_csv('c:/NYC-Taxi-Trip/data/nyc_taxi_trip_duration.csv')

# Clean dataset (drop unnecessary columns, handle missing data)
df_cleaned = df.dropna()

# Fix the id column by removing the 'id' prefix
df_cleaned['id'] = df_cleaned['id'].str.replace('id', '').astype(int)

# Create a connection to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    dbname="nyc_taxi_db",
    user="airflow",
    password="airflow",
    port="5432"
)
cur = connection.cursor()

# Create table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS nyc_taxi_trips (
        id VARCHAR PRIMARY KEY,
        vendor_id INT,
        pickup_datetime TIMESTAMP,
        dropoff_datetime TIMESTAMP,
        passenger_count INT,
        pickup_longitude FLOAT,
        pickup_latitude FLOAT,
        dropoff_longitude FLOAT,
        dropoff_latitude FLOAT,
        store_and_fwd_flag VARCHAR(1),
        trip_duration INT
    )
'''
cur.execute(create_table_query)
connection.commit()

# Insert data into PostgreSQL
insert_query = '''
    INSERT INTO nyc_taxi_trips 
    (id, vendor_id, pickup_datetime, dropoff_datetime, passenger_count, pickup_longitude, pickup_latitude,
    dropoff_longitude, dropoff_latitude, store_and_fwd_flag, trip_duration)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

for _, row in df_cleaned.iterrows():
    cur.execute(insert_query, tuple(row))

# Commit and close the connection
connection.commit()

cur.close()
connection.close()

print("Data loaded successfully!")
