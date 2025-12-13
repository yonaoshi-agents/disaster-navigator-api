from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.schemas.itinerary_schema import ItineraryCreateRequest, ItineraryResponse
from app.services.itinerary_service import itinerary_service

router = APIRouter(
    prefix="/itineraries",
    tags=["itineraries"]
)


@router.post("", response_model=ItineraryResponse, status_code=201)
async def create_itinerary(request: ItineraryCreateRequest):
    """
    旅行日程を作成
    
    ユーザーに紐づいた新しい旅行日程を作成します。
    """
    # 日付の妥当性チェック
    if request.end_date < request.start_date:
        raise HTTPException(
            status_code=400,
            detail="終了日時は開始日時より後である必要があります"
        )
    
    return itinerary_service.create_itinerary(request)


@router.get("", response_model=List[ItineraryResponse])
async def get_itineraries(
    email: Optional[str] = Query(None, description="ユーザーのメールアドレスでフィルタリング")
):
    """
    旅行日程を取得
    
    クエリパラメータでユーザーのメールアドレスを指定すると、
    そのユーザーに紐づく旅行日程のみを取得します。
    指定しない場合は全ての旅行日程を取得します。
    """
    if email:
        return itinerary_service.get_itineraries_by_user(email)
    else:
        return itinerary_service.get_all_itineraries()


@router.get("/{itinerary_id}", response_model=ItineraryResponse)
async def get_itinerary(itinerary_id: str):
    """
    指定されたIDの旅行日程を取得
    """
    itinerary = itinerary_service.get_itinerary_by_id(itinerary_id)
    if not itinerary:
        raise HTTPException(
            status_code=404,
            detail=f"旅行日程が見つかりません: {itinerary_id}"
        )
    return itinerary
