
# Perform proximity analysis using FastAPI

This repository uses python based geoprocessing tools to perform proximity analysis using FASTAPI web framework for building APIs.

# Requirements
Python 3.6+
Postgres database 

pip install fastapi
pip install "uvicorn[standard]"


# Data 

# Run the server with:

Run script main.py from the terminal
uvicorn main:app --reload
Open your browser at : http://127.0.0.1:8000/prox/0 

You will see the JSON response as:

{"Point within the buffer":false}

Pass the values from [0:9] to the url eg: http://127.0.0.1:8000/prox/1

 To check the proximity of each point loaction within the buffer

