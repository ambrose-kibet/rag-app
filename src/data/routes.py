from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.data.service import DataProcessingService
from src.embeddings.service import TextEmbeddingService
from pypdf import PdfReader
from io import BytesIO

data_router = APIRouter()

data_service = DataProcessingService()
text_embedding_service = TextEmbeddingService()


@data_router.post("/ingest/pdf", status_code=201)
async def ingest_pdf(
    file: UploadFile = File(...), session: AsyncSession = Depends(get_session)
):
    try:

        contents = await file.read()
        pdf_reader = PdfReader(BytesIO(contents))
        extracted_text = ""
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                extracted_text += extracted_text

        text_chunks = data_service.split_text(extracted_text)
        for chunk in text_chunks:
            await text_embedding_service.create_text_embedding(session, chunk)
        return {"message": "PDF Ingested"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    pass


@data_router.post("/ingest/url", status_code=201)
async def ingest_url(url: str, session: AsyncSession = Depends(get_session)):
    try:
        extracted_docs = data_service.get_split_document_from_url(url)
        for doc in extracted_docs:
            await text_embedding_service.create_text_embedding(
                session, doc.page_content
            )

        return {"message": "URL Ingested"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    pass
