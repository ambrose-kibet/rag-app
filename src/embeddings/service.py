from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import TextEmbedding

# from langchain_community.vectorstores.pgvector import PGVector
from src.embeddings.schemas import (
    TextEmbedding as TextEmbeddingSchema,
    ReturnTextEmbeddingModel,
)
from src.utils import get_embeddings
from sqlalchemy.future import select


class TextEmbeddingService:

    async def create_text_embedding(
        self, session: AsyncSession, text_embedding: str
    ) -> TextEmbeddingSchema:
        text = text_embedding
        embedding = self.get_text_embedding(text)
        db_text_embedding = TextEmbedding(content=text, embedding=embedding)
        session.add(db_text_embedding)
        await session.commit()
        return db_text_embedding

    async def get_text_embeddings_by_text(
        self, session: AsyncSession, input_text: str
    ) -> list[ReturnTextEmbeddingModel]:
        text = input_text
        query_embedding = self.get_text_embedding(text)

        k = 5
        similarity_threshold = 0.7

        query = (
            select(
                TextEmbedding,
                TextEmbedding.embedding.cosine_distance(query_embedding).label(
                    "distance"
                ),
            )
            .where(
                TextEmbedding.embedding.cosine_distance(query_embedding)
                < similarity_threshold
            )
            .order_by("distance")
            .limit(k)
        )

        result = await session.exec(query)
        results = result.scalars().all()
        res = [
            ReturnTextEmbeddingModel(
                content=result.content,
            )
            for result in results
        ]
        return res

    @staticmethod
    def get_text_embedding(input_text: str) -> list[float]:
        embeddings_instance = get_embeddings()
        text = input_text
        embedding = embeddings_instance.embed_documents([text])[0]
        return embedding
