# Rivian Datagen Demo

The application creates test data in Kafka

This project was generated with Python 3 and Docker.


## Running the Demo
1. Setup Kafak Server as needed - [Kafka Quick Setup][kafkasetup]
1. Obtain Server - can use AWS
1. Install Docker - `sudo apt install docker.io nmon -y`
1. Add Docker Group to User `sudo usermod -a -G docker ubuntu`
1. Relogin for the user to gain access to Docker.
1. Make a local copy of the application code found on [github][github] by `git clone https://github.com/JohnRTurner/riviandatagen.git`
1. Build the Docker image `docker build riviandatagen -t riviandatagen`
1. Run the Image `docker run -d --name riviandatagen -e KAFKA_SERVER=localhost:29092 -e BATCH_SIZE=1000 -e KAFKA_TOPIC=test -e PROC_COUNT=8 -t riviandatagen`
1. View the logs `docker logs -f riviandatagen`


| Option       | Description                   |
|--------------|-------------------------------|
| BATCH_SIZE   | Batch Size                    | 
| KAFKA_TOPIC  | Kafka Topic Name -Will Create |
| PROC_COUNT   | Processes to Concurrently Run |
| KAFKA_SERVER | Kakfka Server                 |         




## Code Description
Can view the code on [github][github]

| Filename                      | Description                                     | 
|-------------------------------|-------------------------------------------------|
| main.py                       | Main module takes parameters and runs generator |
| datagenerators.py             | Creates data and sends to Kafka                 |
| kafka.py                      | wrapper for Kafka calls                         |
| README.md                     | This file                                       |
| Dockerfile                    | Files not to copy to the repository             |
| .dockerignore                 | File to generate docker image                   |
| requirements.txt              | Python library requirements                     |
| kafkasetup/README.md          | Instructions to setup Kafka docker              |
| kafkasetup/docker-compose.yml | Sample docker-compose.yml                       |


[try-free]: https://www.singlestore.com/try-free/
[portal]: https://portal.singlestore.com/
[github]: https://github.com/JohnRTurner/oltpnodejs
[kafkasetup]: kafkasetup/README.md