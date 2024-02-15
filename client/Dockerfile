# Use python 3.10.4
FROM python:3.10.4-alpine3.16

# Set the working directory as /app
WORKDIR /app/

# Copy requirements.txt and package.json to install dependencies
COPY requirements.txt /app/

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the built angular folder and fastapi code
COPY dist/ /app/dist/
COPY server.py /app/