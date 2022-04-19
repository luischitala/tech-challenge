# WIZELINE - GO BOOTCAMP TECH CHALLENGE

## Table of Contents:
- [WIZELINE - GO BOOTCAMP TECH CHALLENGE](#wizeline---go-bootcamp-tech-challenge)
  - [Table of Contents:](#table-of-contents)
  - [Description](#description)
    - [Features](#features)
  - [Lord of the Rings API](#lord-of-the-rings-api)
  - [Requirements:](#requirements)
  - [Relevant Dependencies:](#relevant-dependencies)
  - [Installation](#installation)
    - [With docker](#with-docker)
    - [Without docker](#without-docker)
  - [Run it locally](#run-it-locally)
  - [Basic Usage](#basic-usage)


## Description
This project is a simple REST API made with FastAPI as requirement for the Go Bootcamp from Wizeline.

### Features
Features included:
- Docker, Compose Environment
- Data modeling with pydantic.
- FastAPI Router
- External API connection

## Lord of the Rings API

 In the author's "This massive database will provide you with information about the books, the movie trilogy, many characters and quotes. You are welcome to use the data in your own apps, mixups and (fun) projects "

Link:
https://the-one-api.dev/documentation

*It is required to register to get an api key, in order to be able to access to the private endpoints
https://the-one-api.dev/sign-up

*For this example we will use my key but you can change it on the .env file 

## Requirements:
- Docker and Docker Compose (Optionally)
- Python >= 3.6

## Relevant Dependencies:
- FastAPI == 0.75.2
- Uvicorn == 0.17.6
- Django Environ == 0.8.1
- Httpx == 0.22.0

## Installation
1. Clone or download de repository:
    ```
    $ git clone https://github.com/itastetaco/tech-challenge
    ```

### With docker
1. Run it with Docker Compose.
    ```bash
    docker-compose up
    ```

### Without docker
1. Open the console inside the project directory and create a virtual environment (You can skip this step if you have docker installed).
    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

2. Install the app (You can skip this step if you have docker installed)
    ```bash
    (venv) $ cd /app/v1
    (venv) $ pip install -r requirements.txt
    ```

## Run it locally
    
1. Configure the environment variables into the `.env`.
```bash
# App
SECRET_KEY=6CXIedt4nFvtFADJIAzB  # You can leave this dev key as is.
DEBUG=True  # If DEBUG = True, the reload option of uvicorn will be enabled
PORT=8000  # Server port

```

2. Run the server.
```bash
$ (venv) $ cd /app/v1
$ (venv) python3 main.py
```

## Basic Usage
Once you are running the server open the [Swagger UI App](http://localhost:8000/docs) to checkout the API documentation.

