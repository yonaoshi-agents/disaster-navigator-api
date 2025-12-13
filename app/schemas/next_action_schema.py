from pydantic import BaseModel


class Card(BaseModel):
    id: int
    imageUrl: str
    message: str


class NextActionsResponse(BaseModel):
    cards: list[Card]
