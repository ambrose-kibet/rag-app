import uuid
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel


class Message(BaseModel):
    id: uuid.UUID
    content: str
    message_type: Literal["human", "system"]
    chat_id: str


class CreateMessage(BaseModel):
    content: str
    chat_id: str
    message_type: Literal["human", "system"]


class ChatMessage(BaseModel):
    content: str
