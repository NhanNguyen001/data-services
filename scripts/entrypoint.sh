#!/bin/bash

# Airflow needs to initialize the database
if [ "$1" = "webserver" ]; then
    airflow db init
    airflow users create \
        --username admin \
        --password admin \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com
fi

# Start the requested Airflow component
exec airflow "$@" 