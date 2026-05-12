import json
import time

from kafka import KafkaProducer

producer = None


def get_producer():

    global producer

    while producer is None:

        try:

            producer = KafkaProducer(

                bootstrap_servers="kafka:9092",

                value_serializer=lambda v:
                    json.dumps(v).encode("utf-8")
            )

            print("Kafka producer connected")

        except Exception as e:

            print(
                f"Kafka not ready yet: {e}"
            )

            time.sleep(5)

    return producer


def publish_event(topic, data):

    kafka_producer = get_producer()

    kafka_producer.send(topic, data)

    kafka_producer.flush()