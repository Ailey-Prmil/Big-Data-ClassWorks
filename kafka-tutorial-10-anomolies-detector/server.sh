cd "C:\kafka_2.13-3.9.0" 
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
.\bin\windows\kafka-server-start.bat .\config\server.properties
.\bin\windows\kafka-topics.bat --bootstrap-server localhost:9092 --topic transactions --create --partitions 3 --replication-factor 1
.\bin\windows\kafka-topics.bat --bootstrap-server localhost:9092 --topic anomalies --create --partitions 3 --replication-factor 1


.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic transactions 
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic anomalies 

