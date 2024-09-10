# NYC Taxi Data ETL and Dashboard with Apache Airflow

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
NYC-Taxi-Trip/
│
├── dags/                           # Airflow DAG files
│   ├── nyc_taxi_etl_dag.py         # Main Airflow DAG
│   └── etl_process.py              # ETL Process
│
├── docker-compose.yml              # Docker Compose configuration for Airflow, PostgreSQL, Redis
├── load_dataset.py                 # Script to load data into PostgreSQL
├── dashboard.py                    # Dash dashboard for visualizing the transformed data
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation

# Getting Started
# Prerequisites
Ensure that the following software is installed:
Docker
Python 3.7+
Apache Airflow
PostgreSQL
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/nyc-taxi-trip-etl.git
cd NYC-Taxi-Trip
2. Set Up Docker Compose
Create a .env file (optional) for environment variables, or modify directly in the docker-compose.yml.
Start all services:
bash
Copy code
docker-compose up
This will launch the Airflow webserver, scheduler, PostgreSQL, and Redis services.

3. Load Dataset into PostgreSQL
Ensure the dataset nyc_taxi_trip_duration.csv is in the project root.
Run the data loading script:
bash
Copy code
python load_dataset.py
This will clean the dataset and load it into the nyc_taxi_trips table in PostgreSQL.

4. Run the Airflow DAG
Open Airflow by navigating to http://localhost:8080/.
Trigger the nyc_taxi_etl_dashboard_dag to run the ETL process.
Monitor task status and logs in the Airflow UI.
5. Run the Dashboard
After the ETL pipeline finishes, run the Dash dashboard:

bash
Copy code
python dashboard.py
Visit the dashboard at http://localhost:8050/ to see the visualized data.

Airflow DAG
The DAG consists of three tasks:

Extract Task: Extracts the raw data from PostgreSQL.
Transform Task: Cleans the data, calculates trip distances, and creates a new dataset.
Load Task: Loads the cleaned data into a new table in PostgreSQL for visualization.
Dashboard
The dashboard is built using Dash and Plotly. It displays the following insights:

Trip Duration: Line chart of trip durations over time.
Passenger Count: Bar chart showing the distribution of passenger counts.
Technologies Used
Apache Airflow: Task scheduling and orchestration.
PostgreSQL: Relational database for storing trip data.
Redis: Message broker for handling Airflow tasks.
Docker: Containerization for deploying the services.
Python Dash: Framework for building the interactive dashboard.
Plotly: Visualization library for creating interactive charts.
Running Tests
Unit tests for the ETL scripts can be added to ensure data consistency after extraction and transformation.

Future Enhancements
Include more transformations, such as fare calculations.
Add error handling and logging to the ETL process.
Integrate with other data sources for more insights.
License
This project is licensed under the MIT License.
