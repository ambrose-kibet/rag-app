from langchain_community.document_loaders import FireCrawlLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.config import Config


class DataProcessingService:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )

    def split_text(self, text: str) -> list[str]:
        return self.text_splitter.split_text(text)

    def get_split_document_from_url(self, url: str) -> str:
        loader = FireCrawlLoader(
            api_key=Config.FIRECRAWL_API_KEY, url=url, mode="scrape"
        )
        docs = loader.load()
        for doc in docs:
            for key, value in doc.metadata.items():
                if isinstance(value, list):
                    doc.metadata[key] = ", ".join(map(str, value))

        split_docs = self.text_splitter.split_documents(docs)

        print(f"Sample chunk:\n{split_docs[5].page_content}\n")

        return split_docs
