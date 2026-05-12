# from fastapi import APIRouter
# from app.models import LogData
# from app.database import raw_collection
# from app.kafka_producer import publish_event
# from datetime import datetime
#
# router = APIRouter()
#
#
# # @router.post("/")
# # def ingest_log(data: LogData):
# #
# #     document = {
# #
# #         "source": data.source,
# #
# #         "payload": data.payload,
# #
# #         "normalized": False,
# #
# #         "created_at":
# #             __import__("datetime")
# #             .datetime.utcnow()
# #     }
# #
# #     raw_collection.insert_one(document)
# #
# #     return {
# #         "status": "success",
# #         "message":
# #             f"{data.source} log ingested"
# #     }
#
#
# @router.post("/")
# def ingest_log(data: LogData):
#
#     document = {
#
#         "source": data.source,
#
#         "payload": data.payload,
#
#         "normalized": False,
#
#         # "created_at":
#         #     __import__("datetime")
#         #     .datetime.utcnow()
#         "created at": datetime.utcnow().isoformat()
#
#     }
#
#     raw_collection.insert_one(document)
#
#     publish_event(
#         "raw-security-events",
#         document
#     )
#
#     return {
#         "status": "success",
#         "message":
#             f"{data.source} log ingested "
#             f"and streamed to Kafka"
#     }

from fastapi import APIRouter

from datetime import datetime

from app.models import LogData

from app.database import raw_collection

from app.kafka_producer import publish_event

router = APIRouter()


@router.post("/")
def ingest_log(data: LogData):

    document = {

        "source": data.source,

        "payload": data.payload,

        "normalized": False,

        "created_at":
            datetime.utcnow().isoformat()
    }

    # -----------------------------------
    # Store in MongoDB
    # -----------------------------------

    raw_collection.insert_one(document)

    # -----------------------------------
    # Create Kafka-safe payload
    # -----------------------------------

    kafka_payload = {

        "source": document["source"],

        "payload": document["payload"],

        "normalized":
            document["normalized"],

        "created_at":
            document["created_at"]
    }

    # -----------------------------------
    # Publish to Kafka
    # -----------------------------------

    publish_event(
        "raw-security-events",
        kafka_payload
    )

    return {

        "status": "success",

        "message":
            f"{data.source} log ingested "
            f"and streamed to Kafka"
    }