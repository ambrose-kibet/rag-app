from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.chats.schemas import CreateMessage, Message, ChatMessage
from src.chats.service import MessageService
from src.embeddings.service import TextEmbeddingService
from src.chats.utils import generate_response
import uuid

chat_router = APIRouter()

message_service = MessageService()
text_embedding_service = TextEmbeddingService()


@chat_router.post(
    "/new-chat",
    status_code=status.HTTP_201_CREATED,
)
async def new_chat(
    message: ChatMessage,
    session: AsyncSession = Depends(get_session),
):
    try:

        message_chat_id = str(uuid.uuid4())
        print(message_chat_id)
        message_type = "human"
        new_message = await message_service.create_message(
            session,
            CreateMessage(
                content=message.content,
                message_type=message_type,
                chat_id=message_chat_id,
            ),
        )
        chat_history = []
        response = await generate_response(
            query=message.content, chat_history=chat_history, session=session
        )

        messages = [
            CreateMessage(
                content=message.content,
                message_type="human",
                chat_id=new_message.chat_id,
            ),
            CreateMessage(
                content=response, message_type="system", chat_id=new_message.chat_id
            ),
        ]
        res = await message_service.create_multiple_messages(session, messages)
        return {
            "response": res,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@chat_router.post("/resume-chat/{chat_id}")
async def resume_chat(
    chat_id: str,
    message: ChatMessage,
    session: AsyncSession = Depends(get_session),
):
    try:
        chat_history = await message_service.get_messages_by_chat_id(session, chat_id)
        response = await generate_response(
            query=message.content, chat_history=chat_history, session=session
        )

        messages = [
            CreateMessage(
                content=message.content, message_type="human", chat_id=chat_id
            ),
            CreateMessage(content=response, message_type="system", chat_id=chat_id),
        ]
        res = await message_service.create_multiple_messages(session, messages)
        return {
            "response": res,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@chat_router.get("/chat-history/{chat_id}")
async def chat_history(chat_id: str, session: AsyncSession = Depends(get_session)):
    try:
        chat_history = await message_service.get_messages_by_chat_id(session, chat_id)
        return chat_history
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
