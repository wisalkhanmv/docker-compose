# MLOps (Docker-Compose)

## Overview
This task involves containerizing a web application using Docker Compose and implementing multiple modules within the application.

### Frontend
Design a one-page application that accepts input such as name and email address.

### Backend
Create a Flask endpoint that stores the inserted information (name and email) in the database.

### Database
MongoDB is chosen as the database for this project.

## Instructions
Follow these steps to set up and run the web application:

1. Clone the repository to your local machine.
2. Ensure you have Docker and Docker Compose installed.
3. Navigate to the project directory.
4. Update the necessary configurations in the Dockerfiles and docker-compose.yml if required.
5. Build the Docker images using `docker-compose build`.
6. Run the containers with `docker-compose up`.
7. Access the frontend application at `http://localhost:8081` in your web browser.
8. Enter your name and email address in the input fields provided.
9. Submit the form to store the information in the database through the Flask backend.
10. Verify the data storage functionality by checking the MongoDB database.

## Notes
- Customize the frontend and backend as per your project requirements.
- Ensure that the necessary dependencies are installed in the Docker images.
- Test the application thoroughly to ensure proper functionality.

That's it! You have successfully containerized your web application with Docker Compose and implemented multiple modules.
