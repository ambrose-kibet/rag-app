from pydantic import BaseModel
import uuid


class TextEmbedding(BaseModel):
    id: uuid.UUID
    embedding: list[float]
    content: str


class ReturnTextEmbeddingModel(BaseModel):
    content: str
