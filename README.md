## Prerequisites

- [Docker](https://www.docker.com/) installed on your machine

* [Docker Compose](https://docs.docker.com/compose/) installed on your machine

## Getting Started

Follow these steps to run the Docker container:

**Step 1: Clone the Repository**

Clone this repository to your local machine:

```
git clone git@github.com:AyazYousafxai/generative_ai.git
cd generative_ai
```

Create a `.env` file inside the `generative_ai` folder. Obtain the necessary secrets from the provided email and add them to the `.env` file

**Step 2: Start the Docker Compose Services**

Run the Docker Compose command to start the services defined in the `docker-compose.yml` file:

```
docker-compose up
```

**Step 3: Wait for Model Download (5-10 minutes)**

Wait for 5 to 10 minutes for the `facebook/bart-large-cnn` model to download. The service will start automatically once the downloading is completed.

**Step 4: Access the Application**

Once the services are running and the model is downloaded, you can access the application's documentation by opening a web browser and navigating to:

```
http://localhost:5000/docs
```

**Step 5: Stop the Services**

To stop the services defined in the `docker-compose.yml` file, run:

```
docker-compose down
```

# API Usage Guide

## Description

This guide outlines the usage of the provided API endpoints for user authentication, setting recommendations based on temperature, and retrieving weather summary along with recommendations for a specified city.

## Example Workflow

1. **Signup** : Register a new user account to access protected endpoints.
2. **Login** : Authenticate and obtain an access token.
3. **Set Recommendations** : Use the access token to set recommendations for different temperature ranges in specific cities.
4. **Get Weather and Recommendations** : Retrieve weather summary along with recommendations for a specified city using the access token.

## Endpoints

### User Authentication

**Signup**

* **Method:** POST
* **Endpoint:** `/signup`
* **Description:** Register a new user account.
* **Usage Example:**

```
POST user/signup
{
  "email": "user@example.com",
  "password": "string",
  "name": "string"
}
```

**Login**

* **Method:** POST
* **Endpoint:** `/login`
* **Description:** Authenticate and receive an access token.
* **Usage Example:**

```
POST user/login
{
  "email": "user@example.com",
  "password": "string"
}
```

### Setting Recommendations

**Create Recommendation**

* **Method:** POST
* **Endpoint:** `/recommendations`
* **Description:** Set a recommendation for a city based on temperature.
* **Usage Example:**

```
POST /recommendations
Provide access token in header, city, activities, outfits, and temperature range
```

### Retrieving Weather summary and Recommendations

#### Get summary and Recommendations

* **Method:** GET
* **Endpoint:** `/{city}`
* **Description:** Retrieve weather summary and recommendations for a specific city.
* **Usage Example:**

```
GET /{city}
Provide the city name
```
