# -----------------------------------------------------------------------------
# DOCKERFILE
# -----------------------------------------------------------------------------
# A Dockerfile contains the step-by-step instructions to build a Docker Image.
# Each command (FROM, WORKDIR, COPY) creates a new "Layer" in the image.

# 1. BASE IMAGE
# Always use official, slim images to reduce size and vulnerabilities.
FROM python:3.12-slim

# 2. WORKDIR
# Sets the working directory inside the container. All subsequent commands
# will be executed relative to this path.
WORKDIR /app

# 3. COPY DEPENDENCIES FIRST (Optimization)
# We copy ONLY the requirements file first. Why? Docker caches layers.
# If you change app.py but not requirements.txt, Docker will reuse the cached
# installation layer, saving minutes of build time.
COPY requirements.txt .

# 4. INSTALL DEPENDENCIES
# --no-cache-dir ensures pip doesn't store downloaded tarballs, keeping the image small.
RUN pip install --no-cache-dir -r requirements.txt

# 5. COPY SOURCE CODE
# Now copy the rest of the application code into the container.
COPY . .

# 6. EXPOSE
# This is mainly for documentation. It tells developers which port the app uses.
# It does NOT actually publish the port to the host machine.
EXPOSE 5000

# 7. ENVIRONMENT VARIABLES
# Set environment variables required by the framework.
ENV FLASK_APP=app.py

# 8. CMD (Command)
# The default command that runs when the container starts.
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
