from models.sensor_data import SensorData
from services.score_calculator import ScoreCalculator
from services.sqs_dispatcher import SQSDispatcher
import os
from dotenv import load_dotenv

load_dotenv()
QUEUE_URL = os.getenv("QUEUE_URL")

def main():
    # Simulate sensor reading
    data = SensorData(heart_rate=140, network_type="3G")
    score = ScoreCalculator.calculate(data.heart_rate, data.network_type)

    if score >= 0.9:
        dispatcher = SQSDispatcher(QUEUE_URL)
        payload = data.to_dict() | { "score": score }
        dispatcher.send(payload)
    else:
        print(f"ℹ️ Score {score} below threshold. Data ignored.")

if __name__ == "__main__":
    main()
