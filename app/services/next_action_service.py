from typing import List, Optional
from app.schemas.next_action_schema import Card, NextActionsResponse
from app.services.itinerary_service import itinerary_service
from app.schemas.itinerary_schema import ItineraryResponse


def get_next_actions(email: str, seismic_intensity: str) -> NextActionsResponse:
    """
    Get the list of next actions to take during a disaster.
    Returns mock data with action cards based on seismic intensity.
    
    Args:
        email: ユーザーのメールアドレス
        seismic_intensity: 震度
    
    Returns:
        NextActionsResponse: 次のアクションのリスト
    """
    # ユーザーの旅行日程を取得（LLMに渡す想定で取得のみ）
    user_itineraries: List[ItineraryResponse] = itinerary_service.get_itineraries_by_user(email)
    
    # LLMに震度とユーザーの旅行日程を渡して適切なアクションを生成する想定だが、
    # 現在はパターン別のモックデータを返す

    cards = []

    if seismic_intensity == "0":
        # パターン1: 震度0 (Enjoy your trip!)
        cards = [
            Card(
                id=1,
                imageUrl="https://image/url.here",
                message="Enjoy your trip!"
            )
        ]
    else:
        # パターン2: 震度6- (Safe default for high intensity)
        cards = [
            Card(
                id=1,
                imageUrl="https://image/url.here",
                message="Move away from windows"
            ),
            Card(
                id=2,
                imageUrl="https://image/url.here",
                message="Drop down & Hide under a desk"
            ),
            Card(
                id=3,
                imageUrl="https://image/url.here",
                message="Protect your head"
            ),
            Card(
                id=4,
                imageUrl="https://image/url.here",
                message="Take a deep breath and calm down"
            ),
            Card(
                id=5,
                imageUrl="https://image/url.here",
                message="Wait until the shaking stops"
            ),
        ]
    
    return NextActionsResponse(cards=cards)
