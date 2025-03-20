# Flask Redis Hit Counter

A simple Flask web application that uses Redis to track the number of times the page has been visited. The application runs inside a Docker container and is orchestrated using Docker Compose.

## Features

- Tracks the number of times the page has been visited using Redis.
- Uses Flask as a lightweight web framework.
- Runs inside a Docker container with a Redis service.
- Configured using Docker Compose for easy deployment.

## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

## Getting Started

### 1. Clone the Repository

### 2. Build and Start the Containers

This will:

- Build the Flask web application container.
- Start the Redis container.

### 3. Access the Application

Once the containers are running, open your browser and visit:

Each refresh increases the visit count stored in Redis.

## Stopping the Application

To stop the application, press `CTRL+C` or run:

## Docker Compose Configuration

### `docker-compose.yml`

## Contributing

Feel free to submit pull requests or issues if you find any improvements!

---

Happy coding! 🚀

