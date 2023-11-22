# Use a base python 3.10.13 image which uses alpine 3.18
FROM pytorch/pytorch:2.1.1-cuda12.1-cudnn8-runtime

# Set the working directory to /server inside the docker container
WORKDIR /server

# Copy the required files and stuff
COPY . /server

# Install the dependencies, read more at https://fastapi.tiangolo.com/deployment/docker
RUN pip install --no-cache-dir --upgrade -r requirements.txt