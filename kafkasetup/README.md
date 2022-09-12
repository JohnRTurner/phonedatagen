# KAFKA Setup

## Create Server in AWS
- Server: c6a.2xlarge
- OS: ubuntu 22.04lts

- Tags:

| Tag Name   | Value            |
|------------|------------------|
| Name       | Riven_Test_Kafka |
| Owner      | jturner          |
| CostCenter | SE               |
| Project    | Riven_Test       |

- Key Pair: xxxxx
- Storage: 256G

## Setup Kafka

### Login and upgrade box
```
ssh -i $HOME/Downloads/xxxxx.pem ubuntu@yyyyy.compute-1.amazonaws.com
sudo apt update
sudo apt upgrade -y
```
### Reboot then login and install docker
```
ssh -i $HOME/Downloads/xxxxx.pem ubuntu@yyyyy.compute-1.amazonaws.com
sudo apt install docker.io docker-compose nmon kafkacat -y
sudo usermod -a -G docker ubuntu
exit
```
### Login, docker-compose and run the docker
```
ssh -i $HOME/Downloads/xxxxx.pem ubuntu@yyyyy.compute-1.amazonaws.com
git clone https://github.com/JohnRTurner/riviandatagen.git
cp riviandatagen/kafkasetup/docker-compose.yml .
export MNAME=$(curl http://checkip.amazonaws.com 2>/dev/null |nslookup| grep "name =" |sed "s/.*name = //"|sed "s/.$//")
docker-compose up -d
```
### Create Kafka Topic
| Variable   | Value                                               | Example |
|------------|-----------------------------------------------------|---------|
| Command    | kafka-topics                                        |         |
| topic      | Name of the topic that you wish to create           | test    |
| partitions | Should be 1x, 2x, or 4x the number of db partitions | 128     |
```
docker exec -it ubuntu_kafka-1_1 kafka-topics  --bootstrap-server localhost:29092 --topic test --create --partitions 128 --replication-factor 1
```
## General Instructions
### Stop Kafka
```
docker-compose stop
```
### Start Kafka
```
docker-compose start
```
### List Kafka Topic(s)
```
docker exec -it ubuntu_kafka-1_1 kafka-topics  --bootstrap-server localhost:29092 --list
```
### Delete Kafka Topic
```
docker exec -it ubuntu_kafka-1_1 kafka-topics  --bootstrap-server localhost:29092 --delete --topic test 
```
### Get Topic Size
```
kafkacat -C -b localhost:29092  -t test -o beginning -e -q| wc -l
```
