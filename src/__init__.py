from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.data.routes import data_router
from src.chats.routes import chat_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Creating a new session")
    await init_db()
    yield
    print("Closing the session")


version = "v1"

description = """
A REST API for LD Talent's RAG APP

This REST API is able to;
- create a new chat session  with an  LD talent RAG LLM 
- get all chat sessions
- get a chat session by id
    """

version_prefix = f"/api/{version}"

app = FastAPI(
    title="LD Talent RAG App",
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])


app.include_router(data_router, prefix=version_prefix, tags=["data"])
app.include_router(chat_router, prefix=version_prefix, tags=["chat"])
