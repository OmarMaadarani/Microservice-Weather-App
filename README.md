# Microservice-Weather-App

Simple Python Microservice Weather App using FastAPI

## Setup

1. Clone repo
2. Create Virtual Environment & Install Dependencies
    1. Using VSCode
        1. Open the Repo in VSCode
        2. Follow These Steps: https://code.visualstudio.com/docs/python/environments#_creating-environments
    2. Using PowerShell
        ```
        # Change Directory to where you cloned repo
        cd Microservice-Weather-App
        python -m venv .venv
        .venv\Scripts\activate
        pip install -r requirements.txt
        ```
3. Run the App using Docker-Compose

    In your terminal run

    ```
    docker-compose up -d
    ```

## Endpoints
You access the each API/Microservice through the Nginx Server. Here is a Table of the OpenAPI docs links to each API for you to test the endpoints:
| **API**         | **API URL**                                | **API Docs URL**                           |
|-----------------|--------------------------------------------|--------------------------------------------|
| Forecast        | http://localhost:8080/api/v1/forecast      | http://localhost:8080/api/v1/forecast/docs |
| Current Weather | http://localhost:8080/api/v1/current       | http://localhost:8080/api/v1/current/docs  |
