"""
地震情報サービス
地震情報を取得するビジネスロジック
"""

import random
from app.models.earthquake_model import EarthquakeModel


class EarthquakeService:
    """地震情報サービス"""
    
    # 震度の選択肢
    SEISMIC_INTENSITIES = ["1", "2", "3", "4", "5-", "5+", "6-", "6+", "7"]
    
    def get_earthquake_info(self) -> EarthquakeModel:
        """
        地震情報を取得
        
        Returns:
            EarthquakeModel: 地震情報
        """
        # ランダムに震度を選択
        seismic_intensity = random.choice(self.SEISMIC_INTENSITIES)
        
        return EarthquakeModel(
            seismic_intensity=seismic_intensity,
            disaster_type="earthquake"
        )


# シングルトンインスタンス
earthquake_service = EarthquakeService()
