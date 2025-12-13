from datetime import datetime
from typing import Optional


class Itinerary:
    """旅行日程モデル（内部データ構造）"""
    
    def __init__(
        self,
        itinerary_id: str,
        email: str,
        destination: str,
        start_date: datetime,
        end_date: datetime,
        num_adults: int,
        num_children: int,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.itinerary_id = itinerary_id
        self.email = email
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.num_adults = num_adults
        self.num_children = num_children
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
    
    def to_dict(self) -> dict:
        """辞書形式に変換"""
        return {
            "itinerary_id": self.itinerary_id,
            "email": self.email,
            "destination": self.destination,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "num_adults": self.num_adults,
            "num_children": self.num_children,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
