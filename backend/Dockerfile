#
# Dockerfile for the Resume Analyzer Backend
#
# Author: Wagner Pinheiro
# Date: 2024-07-12
#
# This Dockerfile sets up the environment for the FastAPI backend application.
# It uses a Python 3.9 base image, installs dependencies, and runs the Uvicorn server.
#

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
