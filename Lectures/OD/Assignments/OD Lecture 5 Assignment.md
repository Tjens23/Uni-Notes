---
creation date: 2024-11-09 15:39
modification date: Saturday 9th November 2024 15:39:28
tags:
  - Assignments
year: 2024
semester: 3
links: "[[OD Lecture 5]]"
---

---
# OD Lecture 5 Assignment


---


## Exercise 01: 

```
docker run --name=kafka -p 9092 -d apache/kafka
```


```
docker exec -it <container-id> bash
```

```
cd /opt/kafka/bin && ./kafka-topics.sh --create --bootstrap-server localhost:9092 --topic osds-2024-105
```



## Exercise 02:

```
./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic osds-2024-105
```

in a new window exec into the container and run:

```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic osds-2024-105
```


## Exercise 03 And 04:

```
docker run -d --name zookeeper  -e ZOOKEEPER_CLIENT_PORT=2181  -e ZOOKEEPER_TICK_TIME=2000 confluentinc/cp-zookeeper:latest
```

```
docker run -d  --name kafka  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -p 9092:9092 --link zookeeper confluentinc/cp-kafka:latest
```


test zookeeper 

```
nc -zv localhost 9092
```


```python
from confluent_kafka import Consumer, KafkaException  
  
consumer_config = {  
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'my-group',  
    'auto.offset.reset': 'earliest'  
}  
  
consumer = Consumer(consumer_config)  
consumer.subscribe(['osds-2024-105'])  
  
print("Listening for messages on topic 'osds-2024-105'...")  
try:  
    while True:  
        msg = consumer.poll(1.0)  
        if msg is None:  
            continue  
        if msg.error():  
            raise KafkaException(msg.error())  
        print(f"Received message: {msg.value().decode('utf-8')}")  
except KeyboardInterrupt:  
    pass  
finally:  
    consumer.close()
```