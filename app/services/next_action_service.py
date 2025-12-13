from app.schemas.next_action_schema import Card, NextActionsResponse


def get_next_actions() -> NextActionsResponse:
    """
    Get the list of next actions to take during a disaster.
    Returns mock data with 5 action cards.
    """
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
