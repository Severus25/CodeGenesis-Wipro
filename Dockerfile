# Use an official lightweight Python image as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's layer caching.
# This step will only be re-run if requirements.txt changes.
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container's working directory
COPY . .

# Specify the command to run when the container starts.
# This will execute the main modernization pipeline.
CMD ["python", "main.py"]