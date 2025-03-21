from datetime import datetime

from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.models import Message
from src.chats.schemas import CreateMessage, Message as MessageSchema


class MessageService:
    @staticmethod
    async def create_message(
        session: AsyncSession, message: CreateMessage
    ) -> MessageSchema:
        db_message = Message(
            content=message.content,
            message_type=message.message_type,
            chat_id=message.chat_id,
        )
        session.add(db_message)
        await session.commit()
        return db_message

    @staticmethod
    async def get_messages_by_chat_id(
        session: AsyncSession, chat_id: int
    ) -> list[MessageSchema]:
        result = await session.exec(
            select(Message)
            .where(Message.chat_id == chat_id)
            .order_by(desc(Message.created_at))
        )
        messages = result.all()
        return messages

    @staticmethod
    async def create_multiple_messages(
        session: AsyncSession, messages: list[CreateMessage]
    ) -> list[MessageSchema]:
        db_messages = [
            Message(
                content=message.content,
                message_type=message.message_type,
                chat_id=message.chat_id,
            )
            for message in messages
        ]
        session.add_all(db_messages)
        await session.commit()
        return db_messages
