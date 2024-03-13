# ------------------Code for FlaskAPI----------------------------
# Use the Python 3.10.4 image
FROM python:3.10.4

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Use gunicorn as the entry point to serve the Flask app
CMD ["python", "app.py"]



#-----------------------------*************************FASTAPI************************------------------------

# Code for FastAPI

# # Use the Python 3.10.4 image
# FROM python:3.10.4

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY requirements.txt /app/requirements.txt

# # Install any dependencies specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code into the container at /app
# COPY . /app

# # Expose port 8000 to allow communication to/from server
# EXPOSE 8000

# # Define the command to run your application
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
