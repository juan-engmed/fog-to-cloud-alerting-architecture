from models.sensor_data import SensorData
from services.score_calculator import ScoreCalculator
from services.sns_publisher import SNSPublisher  # novo publisher
import os
from dotenv import load_dotenv

load_dotenv()
TOPIC_ARN = os.getenv("TOPIC_ARN")

def main():
    # Simulate sensor reading
    data = SensorData(heart_rate=140, network_type="3G")
    score = ScoreCalculator.calculate(data.heart_rate, data.network_type)

    if score >= 0.9:
        publisher = SNSPublisher(TOPIC_ARN)
        payload = data.to_dict()
        payload["score"] = score
        publisher.publish(payload)
    else:
        print(f"⚠️ Score {score} below threshold. Data ignored.")

if __name__ == "__main__":
    main()