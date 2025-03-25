from sqlmodel.ext.asyncio.session import AsyncSession
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.output_parser import StrOutputParser
from .schemas import Message
from src.utils import get_model
from src.embeddings.service import TextEmbeddingService
from src.chats.service import MessageService
from src.config import Config
import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


text_embedding_service = TextEmbeddingService()
message_service = MessageService()
llm = get_model()

# based on the chat history to make it a standalone question
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, just "
    "reformulate it if needed and otherwise return it as is."
)

# Create a prompt template for contextualizing questions
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

contextualize_q_chain = contextualize_q_prompt | llm | StrOutputParser()

# Answer question prompt
qa_system_prompt = (
    "You are an assistant for the ld talent organization, answering questions based solely on organizational data retrieved from Slack, Trello, Drive, and similar sources. "
    "Use the following pieces of context to answer the question. If the answer is not supported by the provided context or you do not know the answer, reply with 'I don't know'. "
    "Keep your answer concise and limited to four sentences maximum."
    "\n\n"
    "{context}"
)


qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)


question_answer_chain = qa_prompt | llm | StrOutputParser()


def convert_to_Message_placeholder(
    messages: list[Message],
) -> list[HumanMessage | SystemMessage]:
    return [
        (
            HumanMessage(content=message.content)
            if message.message_type == "human"
            else SystemMessage(content=message.content)
        )
        for message in messages
    ]


async def generate_response(
    query: str, chat_history: list[Message], session: AsyncSession
) -> str:
    chat_history_placeholder = convert_to_Message_placeholder(chat_history)
    # Use the contextualize_q_chain to generate a standalone question
    contextualized_q = contextualize_q_chain.invoke(
        {"input": query, "chat_history": chat_history_placeholder}
    )

    logger.info("Contextualized question: %s", contextualized_q)
    context_docs = await text_embedding_service.get_text_embeddings_by_text(
        session=session, input_text=contextualized_q
    )
    context_docs = [doc.content for doc in context_docs]
    if not context_docs:
        logger.warning("No context documents returned for query: %s", query)
        # add context that no matching info and proceeding to escalate
        # context_docs = ["No matching information found. Escalating to human agent."]
        # send a slack notification to the human agent
        return "No matching information found. Escalating to human agent."

    result = question_answer_chain.invoke(
        {
            "input": query,
            "chat_history": chat_history_placeholder,
            "context": context_docs,
        }
    )
    return result["answer"] if isinstance(result, dict) else result
