# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the frontend application files into the container
COPY . /usr/src/app

# Expose the Flask port (use a different port if 8080 is taken)
EXPOSE 8081

# Install Flask and other dependencies
RUN pip install --no-cache-dir Flask Flask-PyMongo

# Define the command to run the Flask application
CMD ["python", "app.py"]
