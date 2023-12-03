# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the contents of your local Django project directory to the container
COPY . /app

# Install any additional dependencies (if needed)
RUN pip install -r requirements.txt

# Expose the port your Django application runs on (default is 8000)
EXPOSE 8000

# Define the command to run your Django application
CMD ["python", "manage.py", "runserver","0.0.0:8000"]

