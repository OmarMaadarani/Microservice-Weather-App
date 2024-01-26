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
3. Run the Live Uvicorn Server

    In the VSCode Terminal (Which should put you in the Project directory), run the following command

    ```
    cd app/
    uvicorn main:app --reload
    ```
test