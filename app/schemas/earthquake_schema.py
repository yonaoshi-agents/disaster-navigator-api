from pydantic import BaseModel, Field
from typing import Optional


class EarthquakeResponse(BaseModel):
    """地震情報レスポンス"""
    seismic_intensity: str = Field(..., description="震度（例: 5-, 5+, 6-, 6+, 7）")
    disaster_type: str = Field(..., description="災害の種類")
    
    class Config:
        json_schema_extra = {
            "example": {
                "seismic_intensity": "5-",
                "disaster_type": "earthquake"
            }
        }
