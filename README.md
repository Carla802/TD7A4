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

## Run your own containers
### Without Docker Compose

#### Download the mongo image

Pull from Dockerhub the latest mongo image.

`docker pull mongo`

#### Run the mongo container on your network

`docker run --name my-mongo -d --network network1 mongo`

Replace my-mongo with the name of your choice for your mongo container.

#### Build the Docker image of your app

Next, build the Docker image with your Dockerfile :

`docker build -t my-app .`

Replace my-app with the desired name for your image.

#### Bind mount

For the bind mount to work, we need a location where a copy of data.txt is put, so when this file is updated, the web page will contain the changes. We chose here our Desktop.

`cp data.txt /Users/<your username>/Desktop`

Replace <your username> by your username.

#### Run a container using the Docker image

To run a container using the Docker image, use the following command:

`docker run --name my-flask-app -d --network network1 -p 5001:5000 -v /Users/<your username>/Desktop/data.txt:/app/data.txt my-app`

Replace my-flask-app with the desired name for your container and my-app with the name of the Docker image you built earlier.
Replace "your username" by your username.

Now that our two containers are running, you can check your web page on localhost:5001. On the default route, you can see the content of your mongo database, and on the /td6 route, the content of your data.txt file.

If you modify the data.txt in your Desktop, save it and refresh your web page, you will see the changes.

### Using Docker Compose

Instead of running containers manually, you can use Docker Compose to manage your containers more easily.

#### Run the containers

To get your Docker image created and run the containers defined in the Docker Compose configuration, use the following command:

`docker-compose up --build`

Now, our app is running on localhost:5000

On the default route, you can see the content of your database, and on the /td6 route the content of data.txt.
If you modify the data.txt inside your TD7A4 directory, save it and refresh your page, the changes will appear.

#### Stop the containers

To stop the containers, use the following command:

`docker-compose down`

This will stop and remove all containers defined in the Docker Compose configuration.

Congratulations! You have now successfully built and run containers using our Docker image and Docker Compose.
