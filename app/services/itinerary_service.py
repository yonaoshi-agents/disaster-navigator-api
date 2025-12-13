from typing import List, Optional
from datetime import datetime
import uuid
from app.models.itinerary_model import Itinerary
from app.schemas.itinerary_schema import ItineraryCreateRequest, ItineraryResponse


class ItineraryService:
    """旅行日程サービス"""
    
    def __init__(self):
        # インメモリストレージ（本番環境ではデータベースを使用）
        self._itineraries: dict[str, Itinerary] = {}
    
    def create_itinerary(self, request: ItineraryCreateRequest) -> ItineraryResponse:
        """
        旅行日程を作成
        
        Args:
            request: 旅行日程作成リクエスト
            
        Returns:
            作成された旅行日程のレスポンス
        """
        # ユニークなIDを生成
        itinerary_id = f"itin_{uuid.uuid4().hex[:12]}"
        
        # 旅行日程モデルを作成
        itinerary = Itinerary(
            itinerary_id=itinerary_id,
            user_mailaddress=request.user_mailaddress,
            title=request.title,
            destination=request.destination,
            start_date=request.start_date,
            end_date=request.end_date,
            companions=request.companions,
            participants=[p.model_dump() for p in request.participants],
            description=request.description
        )
        
        # ストレージに保存
        self._itineraries[itinerary_id] = itinerary
        
        # レスポンスを返す
        return ItineraryResponse(**itinerary.to_dict())
    
    def get_itinerary_by_id(self, itinerary_id: str) -> Optional[ItineraryResponse]:
        """
        IDで旅行日程を取得
        
        Args:
            itinerary_id: 旅行日程ID
            
        Returns:
            旅行日程のレスポンス、見つからない場合はNone
        """
        itinerary = self._itineraries.get(itinerary_id)
        if itinerary:
            return ItineraryResponse(**itinerary.to_dict())
        return None
    
    def get_itineraries_by_user(self, user_mailaddress: str) -> List[ItineraryResponse]:
        """
        ユーザーに紐づく旅行日程を全て取得
        
        Args:
            user_mailaddress: ユーザーのメールアドレス
            
        Returns:
            旅行日程のリスト
        """
        user_itineraries = [
            ItineraryResponse(**itinerary.to_dict())
            for itinerary in self._itineraries.values()
            if itinerary.user_mailaddress == user_mailaddress
        ]
        return user_itineraries
    
    def get_all_itineraries(self) -> List[ItineraryResponse]:
        """
        全ての旅行日程を取得
        
        Returns:
            全旅行日程のリスト
        """
        return [
            ItineraryResponse(**itinerary.to_dict())
            for itinerary in self._itineraries.values()
        ]


# サービスのシングルトンインスタンス
itinerary_service = ItineraryService()
