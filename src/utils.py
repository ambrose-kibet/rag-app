from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from .config import Config

_model_instance = None


def get_model():
    """Lazy initialisation of ChatOpenAI instance."""
    global _model_instance
    if _model_instance is None:
        _model_instance = ChatOpenAI(
            model="gpt-3.5-turbo", api_key=Config.OPENAI_API_KEY
        )
    return _model_instance


_embeddings_instance = None


def get_embeddings():
    """Lazy initialisation of OpenAIEmbeddings instance."""
    global _embeddings_instance
    if _embeddings_instance is None:
        _embeddings_instance = OpenAIEmbeddings(
            model="text-embedding-3-small", api_key=Config.OPENAI_API_KEY
        )
    return _embeddings_instance
