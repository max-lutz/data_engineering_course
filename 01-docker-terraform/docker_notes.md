# Docker

Delivers software in packages called containers. Containers are isolated from one another.

A docker image is a snapshot of a container and has all the instructions to run this container. --> Virtualized OS.

Docker helps with:
- reproducibility
- local experiments
- Integration tests (CI/CD)
- Running pipelines on the cloud
- Spark
- Serverless

A pipeline is a process that ingests data and produces data.


Kill all containers:
`docker kill $(docker ps -q)`


Create docker image
`docker build -t [docker_image] .`

Run docker image in interactive mode:
`docker container run -it [docker_image] /bin/bash`

![alt text](../images/dockercheatsheet8.png "Title")

