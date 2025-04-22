import boto3
import json
from typing import Any

class SNSPublisher:
    def __init__(self, topic_arn: str):
        self.topic_arn = topic_arn
        self.client = boto3.client("sns")

    def publish(self, message: dict[str, Any]) -> None:
        response = self.client.publish(
            TopicArn=self.topic_arn,
            Message=json.dumps(message)
        )
        print(f"📢 Message published to SNS: {response['MessageId']}")