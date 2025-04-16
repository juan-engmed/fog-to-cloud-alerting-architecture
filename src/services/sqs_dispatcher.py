import boto3
import json
from typing import Any

class SQSDispatcher:
    def __init__(self, queue_url: str):
        self.queue_url = queue_url
        self.client = boto3.client("sqs")

    def send(self, message: dict[str, Any]) -> None:
        response = self.client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(message)
        )
        print(f"✅ Message sent to SQS: {response['MessageId']}")