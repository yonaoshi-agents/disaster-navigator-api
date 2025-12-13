from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Participant(BaseModel):
    """参加者情報"""
    name: str = Field(..., min_length=1, description="参加者の名前")
    age: Optional[int] = Field(None, ge=0, description="年齢")
    relationship: Optional[str] = Field(None, description="主催者との関係（例：本人、家族、友人、同僚）")
    notes: Optional[str] = Field(None, description="備考（例：食物アレルギー、特記事項など）")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "山田太郎",
                "age": 35,
                "relationship": "本人",
                "notes": "なし"
            }
        }


class ItineraryCreateRequest(BaseModel):
    """旅行日程作成リクエスト"""
    user_mailaddress: str = Field(..., description="ユーザーのメールアドレス")
    title: str = Field(..., min_length=1, description="旅行タイトル")
    destination: str = Field(..., min_length=1, description="目的地")
    start_date: datetime = Field(..., description="開始日時")
    end_date: datetime = Field(..., description="終了日時")
    companions: Optional[str] = Field(None, description="誰と行くか（例：家族、友人、恋人、一人旅）")
    participants: List[Participant] = Field(default_factory=list, description="参加者の詳細情報")
    description: Optional[str] = Field(None, description="旅行の説明")
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_mailaddress": "yamada@example.com",
                "title": "東京観光",
                "destination": "東京",
                "start_date": "2025-12-20T09:00:00",
                "end_date": "2025-12-22T18:00:00",
                "companions": "家族",
                "participants": [
                    {"name": "山田太郎", "age": 35, "relationship": "本人", "notes": "なし"},
                    {"name": "山田花子", "age": 33, "relationship": "配偶者", "notes": "なし"},
                    {"name": "山田一郎", "age": 8, "relationship": "子供", "notes": "卵アレルギー"},
                    {"name": "山田二郎", "age": 5, "relationship": "子供", "notes": "なし"}
                ],
                "description": "年末の東京観光旅行"
            }
        }


class ItineraryResponse(BaseModel):
    """旅行日程レスポンス"""
    itinerary_id: str = Field(..., description="旅行日程ID")
    user_mailaddress: str = Field(..., description="ユーザーのメールアドレス")
    title: str = Field(..., description="旅行タイトル")
    destination: str = Field(..., description="目的地")
    start_date: datetime = Field(..., description="開始日時")
    end_date: datetime = Field(..., description="終了日時")
    companions: Optional[str] = Field(None, description="誰と行くか（例：家族、友人、恋人、一人旅）")
    participants: List[Participant] = Field(default_factory=list, description="参加者の詳細情報")
    number_of_people: int = Field(..., description="参加人数（participantsから自動計算）")
    description: Optional[str] = Field(None, description="旅行の説明")
    created_at: datetime = Field(..., description="作成日時")
    updated_at: datetime = Field(..., description="更新日時")
    
    class Config:
        json_schema_extra = {
            "example": {
                "itinerary_id": "itin_123456",
                "user_mailaddress": "yamada@example.com",
                "title": "東京観光",
                "destination": "東京",
                "start_date": "2025-12-20T09:00:00",
                "end_date": "2025-12-22T18:00:00",
                "companions": "家族",
                "participants": [
                    {"name": "山田太郎", "age": 35, "relationship": "本人", "notes": "なし"},
                    {"name": "山田花子", "age": 33, "relationship": "配偶者", "notes": "なし"},
                    {"name": "山田一郎", "age": 8, "relationship": "子供", "notes": "卵アレルギー"},
                    {"name": "山田二郎", "age": 5, "relationship": "子供", "notes": "なし"}
                ],
                "number_of_people": 4,
                "description": "年末の東京観光旅行",
                "created_at": "2025-12-13T10:00:00",
                "updated_at": "2025-12-13T10:00:00"
            }
        }
