# Robotics-Docker-Task-Firas

**This repository contains the assignment for session 3 of the robotics path.**

`answers.md` contains the answers of the posed questions on Docker, and the rest of the files are used for the Docker project.

The Docker project is composed of 3 services: Python, MinIO, and Redis. The Python service is used to create and upload a randomly generated image onto the MinIO database. The Redis service is used to keep track of the number of files, which is useful when writing the image to the database because it prevents overwriting existing files.

A `healthcheck` is a way to define a command that regularly checks on the health of a container. It helps ensure the container is operational and ready to handle requests or perform its intended functions.

In this project, a `healthcheck` is used on the Python service to periodically upload random image every 30 seconds. The `healthcheck.py` Python script contains the code which will run when the `healthcheck` in the Docker Compose file is invoked. If the script fails, it will print an error message on the port connected to the Python app.

Finally, this Docker project uses two volumes to persist data. One is used for the MinIO service and the other for the Redis service. This way, the files on the MinIO database are not lost when the project is down, and the file counter is persisted as well.

