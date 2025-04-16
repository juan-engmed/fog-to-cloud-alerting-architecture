class ScoreCalculator:
    @staticmethod
    def calculate(heart_rate: int, network_type: str) -> float:
        score = 0.0
        if heart_rate > 130:
            score += 0.6
        if network_type.upper() == "3G":
            score += 0.4
        elif network_type.upper() == "4G":
            score += 0.2
        elif network_type.upper() == "WI-FI":
            score += 0.1
        return round(score, 2)