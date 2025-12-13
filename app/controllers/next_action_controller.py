from fastapi import APIRouter, Query
from typing import Optional

from app.schemas.next_action_schema import NextActionsResponse
from app.services.next_action_service import get_next_actions

router = APIRouter()


@router.get("/next-actions", response_model=NextActionsResponse)
def get_next_actions_endpoint(
    email: str = Query(..., description="ユーザーのメールアドレス"),
    seismic_intensity: str = Query(..., description="震度（例: 5-, 5+, 6-, 6+, 7）")
):
    """
    Get the list of next actions to take during a disaster.
    
    Args:
        email: ユーザーのメールアドレス
        seismic_intensity: 震度
    
    Returns:
        NextActionsResponse: A response containing a list of action cards
    """
    return get_next_actions(email=email, seismic_intensity=seismic_intensity)
