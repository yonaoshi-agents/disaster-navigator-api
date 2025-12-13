from fastapi import APIRouter

from app.schemas.next_action_schema import NextActionsResponse
from app.services.next_action_service import get_next_actions

router = APIRouter()


@router.get("/next-actions", response_model=NextActionsResponse)
def get_next_actions_endpoint():
    """
    Get the list of next actions to take during a disaster.
    
    Returns:
        NextActionsResponse: A response containing a list of action cards
    """
    return get_next_actions()
