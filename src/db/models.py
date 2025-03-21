import uuid
from datetime import datetime

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, SQLModel
from pgvector.sqlalchemy import Vector

N_DIM = 1536


class Message(SQLModel, table=True):
    id: str = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    content: str
    message_type: str = Field(
        sa_column=Column(
            pg.ENUM("human", "system", name="message_type"), nullable=False
        )
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    chat_id: str


class TextEmbedding(SQLModel, table=True):
    id: str = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    embedding: Vector = Field(sa_column=Column(Vector(N_DIM)))
    content: str = Field(sa_column=Column(pg.TEXT))

    class Config:
        arbitrary_types_allowed = True
