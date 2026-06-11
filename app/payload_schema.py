# app/payload_schema.py

from datetime import datetime
import uuid


def create_payload(

    command_name,

    confidence,

    module_name,

    source_identifier,

    threshold=0.70

):

    payload = {

        "timestamp":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "session_id":
        str(uuid.uuid4()),

        "command_name":
        command_name,

        "module_name":
        module_name,

        "source_identifier":
        source_identifier,

        "confidence":
        confidence,

        "threshold":
        threshold
    }

    return payload