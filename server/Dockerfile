# Use a base python 3.10.13 image which uses alpine 3.18
FROM python:3.10.13-alpine3.18

# Set the working directory to /server inside the docker container
WORKDIR /server

# Copy the required files and stuff
COPY . /server

# Install the dependencies, read more at https://fastapi.tiangolo.com/deployment/docker
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the port 5000
EXPOSE 5000

# Set the command to start the FastAPI server in production
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
