from pydantic import BaseModel
from typing import List

class SessionRequest(BaseModel):
    chips: List[str]

class ReflectionRequest(BaseModel):
    session_id: str
    card_index: int
    reflection_text: str
