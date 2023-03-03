# TD7A4

## Prerequisites
Before starting, you'll need to have the following tools installed on your system:

- Docker
- Docker Compose


## Clone the repository

First, clone the repository containing our Docker image and Docker Compose configuration:

`git clone https://github.com/Carla802/TD7A4.git`

And go inside the new directory

`cd TD7A4`

## Create a bridge network

Create a bridge network with the name of your choice. We choose network1 here.

`docker network create --driver bridge network1`

## Download the mongo image

Pull from the Dockerghub the latest mongo image.

`docker pull mongo`

## Run the mongo container on your network

`docker run --name my-mongo -d --network network1 mongo``

## Build the Docker image of your app

Next, navigate to the directory containing the Dockerfile and build the Docker image:

docker build -t my-image .

Replace my-image with the desired name for your image.

## Run a container using the Docker image

To run a container using the Docker image, use the following command:

`docker run --name my-flask-app -d --network network1 -p 5001:5000 -v /Users/carla/Desktop/data.txt:/app/data.txt my-flask-app`

Replace my-container with the desired name for your container and my-image with the name of the Docker image you built earlier.

Using Docker Compose
Instead of running containers manually, you can use Docker Compose to manage your containers more easily.

Build the Docker Compose configuration
Before you can use Docker Compose, you need to build the Docker image using the following command:

Copy code
docker-compose build
Run the containers
To run the containers defined in the Docker Compose configuration, use the following command:

Copy code
docker-compose up -d
This will start all containers in detached mode.

Stop the containers
To stop the containers, use the following command:

Copy code
docker-compose down
This will stop and remove all containers defined in the Docker Compose configuration.

Congratulations! You have now successfully built and run containers using our Docker image and Docker Compose.
