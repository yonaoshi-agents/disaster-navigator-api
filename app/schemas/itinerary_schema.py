from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ItineraryCreateRequest(BaseModel):
    """旅行日程作成リクエスト"""
    email: str = Field(..., description="ユーザーのメールアドレス")
    destination: str = Field(..., min_length=1, description="目的地")
    start_date: datetime = Field(..., description="開始日時")
    end_date: datetime = Field(..., description="終了日時")
    num_adults: int = Field(..., ge=0, description="大人の人数")
    num_children: int = Field(..., ge=0, description="子供の人数")
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "yamada@example.com",
                "destination": "東京",
                "start_date": "2025-12-20T09:00:00",
                "end_date": "2025-12-22T18:00:00",
                "num_adults": 2,
                "num_children": 2
            }
        }


class ItineraryResponse(BaseModel):
    """旅行日程レスポンス"""
    itinerary_id: str = Field(..., description="旅行日程ID")
    email: str = Field(..., description="ユーザーのメールアドレス")
    destination: str = Field(..., description="目的地")
    start_date: datetime = Field(..., description="開始日時")
    end_date: datetime = Field(..., description="終了日時")
    num_adults: int = Field(..., description="大人の人数")
    num_children: int = Field(..., description="子供の人数")
    created_at: datetime = Field(..., description="作成日時")
    updated_at: datetime = Field(..., description="更新日時")
    
    class Config:
        json_schema_extra = {
            "example": {
                "itinerary_id": "itin_123456",
                "email": "yamada@example.com",
                "destination": "東京",
                "start_date": "2025-12-20T09:00:00",
                "end_date": "2025-12-22T18:00:00",
                "num_adults": 2,
                "num_children": 2,
                "created_at": "2025-12-13T10:00:00",
                "updated_at": "2025-12-13T10:00:00"
            }
        }
