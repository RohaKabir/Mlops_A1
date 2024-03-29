# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY code/model.py .

# Install dependencies
RUN pip install scikit-learn

# Command to run the Python script
CMD ["python", "model.py"]
