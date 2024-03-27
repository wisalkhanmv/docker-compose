# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY ./requirements.txt /usr/src/app/

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /usr/src/app

# Expose the Flask port
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
