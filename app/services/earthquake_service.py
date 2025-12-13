"""
地震情報サービス
地震情報を取得するビジネスロジック
"""

import random
from itertools import cycle
from app.models.earthquake_model import EarthquakeModel


class EarthquakeService:
    """地震情報サービス"""
    
    # 震度の選択肢
    SEISMIC_INTENSITIES = ["3", "4", "6-"]
    
    def __init__(self):
        # 無限にループするイテレータを作成
        self._intensity_cycle = cycle(self.SEISMIC_INTENSITIES)

    def get_earthquake_info(self) -> EarthquakeModel:
        """
        地震情報を取得
        
        Returns:
            EarthquakeModel: 地震情報
        """
        # 順番に震度を選択
        seismic_intensity = next(self._intensity_cycle)
        
        return EarthquakeModel(
            seismic_intensity=seismic_intensity,
            disaster_type="earthquake"
        )


# シングルトンインスタンス
earthquake_service = EarthquakeService()
