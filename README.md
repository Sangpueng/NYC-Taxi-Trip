# NewYorkCity-Taxi-Trip: ETL and Dashboard with Apache Airflow

# Overview
This project demonstrates the use of Apache Airflow to build an ETL (Extract, Transform, Load) pipeline for the NYC Taxi Dataset. The pipeline automates data ingestion, transformation, and storage in a PostgreSQL database, and the transformed data is visualized using Python Dash for real-time insights.

# Features
- Automated ETL Pipeline: Apache Airflow is used to orchestrate the entire ETL process, which extracts, transforms, and loads data into a PostgreSQL database.
- Data Storage with PostgreSQL: Data from the NYC Taxi dataset is stored in a PostgreSQL database and managed using SQL queries.
- Data Visualization with Dash: An interactive dashboard is developed using Python Dash to visualize trip duration and other metrics.
- Dockerized Deployment: The entire project, including Airflow, PostgreSQL, and Redis, is containerized using Docker for easy deployment and scalability.

# Architecture
1. Extract: Data is extracted from CSV files containing NYC Taxi trip records.
2. Transform: The data is cleaned and transformed to calculate trip duration and distance.
3. Load: The cleaned data is loaded into the nyc_taxi_db PostgreSQL database for storage.
4. Dashboard: The dashboard provides insights on key metrics like trip duration, number of passengers, etc., with interactive visualizations built using Dash and Plotly.

# Project Structure
![image](https://github.com/user-attachments/assets/d61da559-8795-4fcd-8642-42bb124f1e9f)

# Getting Started
# Prerequisites
Ensure that the following software is installed:
- Docker
- Python 3.7+
- Apache Airflow
- PostgreSQL

# 1. Clone the Repository
![image](https://github.com/user-attachments/assets/10ccf802-0803-4626-8e12-0f6870ee3a28)

# 2. Set Up Docker Compose
  1. Create a .env file (optional) for environment variables, or modify directly in the docker-compose.yml.
  2. Start all services: ![image](https://github.com/user-attachments/assets/09e1b0e6-2393-4c22-ba8f-2df307fa3fff)

This will launch the Airflow webserver, scheduler, PostgreSQL, and Redis services.

# 3. Load Dataset into PostgreSQL
- Ensure the dataset nyc_taxi_trip_duration.csv is in the project root.
- Run the data loading script: ![image](https://github.com/user-attachments/assets/ec8225e7-b6ee-42a9-9818-53c69651511c)

This will clean the dataset and load it into the nyc_taxi_trips table in PostgreSQL.

# 4. Run the Airflow DAG
- Open Airflow by navigating to http://localhost:8080/.
- Trigger the nyc_taxi_etl_dashboard_dag to run the ETL process.
- Monitor task status and logs in the Airflow UI.

# 5. Run the Dashboard
After the ETL pipeline finishes, run the Dash dashboard: ![image](https://github.com/user-attachments/assets/e6613c04-a4db-4dbf-be00-2dfbc8df2228)

Visit the dashboard at http://localhost:8050/ or http://127.0.0.1:8050/ to see the visualized data.

# Airflow DAG
The DAG consists of three tasks:

1. Extract Task: Extracts the raw data from PostgreSQL.
2. Transform Task: Cleans the data, calculates trip distances, and creates a new dataset.
3. Load Task: Loads the cleaned data into a new table in PostgreSQL for visualization.

# Dashboard
The dashboard is built using Dash and Plotly. It displays the following insights:
- Trip Duration: Line chart of trip durations over time.
- Passenger Count: Bar chart showing the distribution of passenger counts.

![image](https://github.com/user-attachments/assets/4b5fac73-bc20-4b67-b036-cd60ee710167)

# Technologies Used
- Apache Airflow: Task scheduling and orchestration.
- PostgreSQL: Relational database for storing trip data.
- Redis: Message broker for handling Airflow tasks.
- Docker: Containerization for deploying the services.
- Python Dash: Framework for building the interactive dashboard.
- Plotly: Visualization library for creating interactive charts.

# Running Tests
Unit tests for the ETL scripts can be added to ensure data consistency after extraction and transformation.

# Future Enhancements
- Include more transformations, such as fare calculations.
- Add error handling and logging to the ETL process.
- Integrate with other data sources for more insights.

