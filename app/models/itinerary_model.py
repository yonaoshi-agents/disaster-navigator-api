from datetime import datetime
from typing import Optional, List, Any


class Itinerary:
    """旅行日程モデル（内部データ構造）"""
    
    def __init__(
        self,
        itinerary_id: str,
        user_mailaddress: str,
        title: str,
        destination: str,
        start_date: datetime,
        end_date: datetime,
        companions: Optional[str] = None,
        participants: Optional[List[dict]] = None,
        description: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.itinerary_id = itinerary_id
        self.user_mailaddress = user_mailaddress
        self.title = title
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.companions = companions
        self.participants = participants or []
        self.description = description
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
    
    def to_dict(self) -> dict:
        """辞書形式に変換"""
        return {
            "itinerary_id": self.itinerary_id,
            "user_mailaddress": self.user_mailaddress,
            "title": self.title,
            "destination": self.destination,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "companions": self.companions,
            "participants": self.participants,
            "number_of_people": len(self.participants),
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
