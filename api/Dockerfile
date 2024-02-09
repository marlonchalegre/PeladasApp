# Use the official Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the API will run
EXPOSE 8000

RUN ["python", "manage.py", "migrate"]
# Set the command to run the API when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
