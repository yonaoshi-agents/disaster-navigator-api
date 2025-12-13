from typing import List, Optional
from app.schemas.next_action_schema import Card, NextActionsResponse
from app.services.itinerary_service import itinerary_service
from app.schemas.itinerary_schema import ItineraryResponse


def get_next_actions(email: str, seismic_intensity: str) -> NextActionsResponse:
    """
    Get the list of next actions to take during a disaster.
    Returns mock data with 5 action cards.
    
    Args:
        email: ユーザーのメールアドレス
        seismic_intensity: 震度
    
    Returns:
        NextActionsResponse: 次のアクションのリスト
    """
    # ユーザーの旅行日程を取得（LLMに渡す想定で取得のみ）
    user_itineraries: List[ItineraryResponse] = itinerary_service.get_itineraries_by_user(email)
    
    # TODO: LLMに震度とユーザーの旅行日程を渡して適切なアクションを生成
    # 現在は震度とユーザー日程を取得するのみで、モックデータを返す
    
    cards = [
        Card(
            id=1,
            imageUrl="https://image/url.here",
            message="Move away from windows and heavy furniture"
        ),
        Card(
            id=2,
            imageUrl="https://image/url.here",
            message="Get under a table if shaking continues"
        ),
        Card(
            id=3,
            imageUrl="https://image/url.here",
            message="Charge your smartphone"
        ),
        Card(
            id=4,
            imageUrl="https://image/url.here",
            message="Check evacuation routes"
        ),
        Card(
            id=5,
            imageUrl="https://image/url.here",
            message="Prepare emergency supplies"
        ),
    ]
    
    return NextActionsResponse(cards=cards)
