# CA4
    # This repository contains a Flask-based web application for user login. The application manages usernames and passwords with an HTML frontend and an SQL backend.
# Docker Images
    #  The Docker images for this project are as follows:

        # Web Server Image: mlflops/docker_web:2.0
        # Database Image: mlflops/database_container:2

# Running the Docker Compose Stack
    # To run the Docker Compose stack for this web application, follow these steps:

#    1. Clone the Repository:
    git clone https://github.com/yourusername/CA4.git
    cd CA4
#    2. Update Environment Variables:
    # Before running the Docker Compose stack, you need to set up environment variables. Create a .env file in the root of the repository and add the following:
    # Database connection details
    DATABASE_URI=mysql://root:bmsmlops123@db/database

#    3. Create network:
    docker network create webapp_db_network
    
#    3. Build and Start the Docker Containers:
    docker-compose up --build
#    4. Access the Web Application:
    # Open your web browser and go to http://localhost:5000/ to access the web application.

#    5. Stopping the Stack:
    # To stop the Docker Compose stack and remove the containers, use the following command:
    docker-compose down
