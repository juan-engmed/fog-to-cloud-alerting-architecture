class SensorData:
    def __init__(self, heart_rate: int, network_type: str):
        self.heart_rate = heart_rate
        self.network_type = network_type.upper()

    def to_dict(self) -> dict:
        return {
            "heart_rate": self.heart_rate,
            "network_type": self.network_type
        }