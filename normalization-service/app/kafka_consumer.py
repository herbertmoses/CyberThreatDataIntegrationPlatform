import json
import time

from kafka import KafkaConsumer

from app.database import (
    normalized_collection
)

from app.normalizers.edr import (
    normalize_edr
)

from app.normalizers.cloud import (
    normalize_cloud
)

from app.normalizers.cicd import (
    normalize_cicd
)


# -----------------------------------
# Kafka Consumer Connection
# -----------------------------------

def get_consumer():

    while True:

        try:

            consumer = KafkaConsumer(

                "raw-security-events",

                bootstrap_servers="kafka:9092",

                auto_offset_reset="earliest",

                value_deserializer=lambda m:
                    json.loads(
                        m.decode("utf-8")
                    )
            )

            print(
                "Kafka consumer connected"
            )

            return consumer

        except Exception as e:

            print(
                f"Kafka not ready yet: {e}"
            )

            time.sleep(5)


# -----------------------------------
# Consume Streaming Events
# -----------------------------------

def consume_events():

    consumer = get_consumer()

    print(
        "Kafka normalization consumer started..."
    )

    for message in consumer:

        log = message.value

        source = log.get("source")

        normalized = None

        # -------------------------------
        # EDR
        # -------------------------------

        if source == "edr":

            normalized = normalize_edr(log)

        # -------------------------------
        # Cloud
        # -------------------------------

        elif source == "cloud":

            normalized = normalize_cloud(log)

        # -------------------------------
        # CI/CD
        # -------------------------------

        elif source == "cicd":

            normalized = normalize_cicd(log)

        # -------------------------------
        # Insert Deduplicated Event
        # -------------------------------

        if normalized:

            existing = (
                normalized_collection.find_one(
                    {
                        "event_hash":
                            normalized[
                                "event_hash"
                            ]
                    }
                )
            )

            if existing:

                print(
                    "Duplicate event skipped"
                )

                continue

            normalized_collection.insert_one(
                normalized
            )

            print(
                "Normalized event inserted"
            )