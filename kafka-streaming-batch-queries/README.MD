# STEPS TO RUN KAFKA

1. Download kafka via: https://downloads.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
2. Extract the file to: C:/
3. Open terminal and run:

```
cd C:/kafka_2.13-3.9.0

.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

.\bin\windows\kafka-server-start.bat .\config\server.properties

.\bin\windows\kafka-topics.bat --create --topic Number --bootstrap-server localhost:9092
```
