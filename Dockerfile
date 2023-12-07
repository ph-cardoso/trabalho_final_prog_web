# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-dev

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run your application using Poetry and uvicorn with reload
CMD ["poetry", "run", "uvicorn", "trabalho_final_prog_web.__main__:app", "--host", "0.0.0.0", "--port", "8000"]
