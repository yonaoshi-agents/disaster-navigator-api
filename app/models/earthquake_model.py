"""
地震情報のモデル定義
"""


class EarthquakeModel:
    """地震情報モデル"""
    
    def __init__(self, seismic_intensity: str, disaster_type: str = "earthquake"):
        """
        Args:
            seismic_intensity: 震度（例: 5-, 5+, 6-, 6+, 7）
            disaster_type: 災害の種類（デフォルト: earthquake）
        """
        self.seismic_intensity = seismic_intensity
        self.disaster_type = disaster_type
    
    def to_dict(self) -> dict:
        """辞書形式に変換"""
        return {
            "seismic_intensity": self.seismic_intensity,
            "disaster_type": self.disaster_type
        }
