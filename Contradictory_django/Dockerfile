# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code into the container
COPY . /app/

# Copy the model file into the container
COPY content/ /app/model/

# Expose port 8000 (adjust as per your Django app's configuration)
EXPOSE 8000

# Run the development server (replace "Contradictory_django" with your Django project name)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
