# src/backend/pdf_processor.py
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

from vector_db.db_handler import get_vector_db


class PDFProcessor:
    def __init__(self):
        self.vector_db = get_vector_db()

    def load(self, file_path: str) -> str:
        """load PDF and extract text from file"""
        loader = PyPDFLoader(file_path)
        text = ""
        for page in loader.alazy_load():
            text += page.page_content
        return text

    def split(self, text: str) -> list[str]:
        """split whole text into chunks"""
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            encoding_name="cl100k_base", chunk_size=200, chunk_overlap=0
        )
        return text_splitter.split_text(text)

    def store(self, file_path: str) -> str:
        """store chunks into vector DB"""
        text = self.load(file_path)
        texts = self.split(text)
        self.vector_db.add_texts(texts)
        return f"File {file_path} has stored in Milvus"

    def process_multiple_pdfs(self, file_paths: list[str]) -> list[str]:
        """process multiple PDFs"""
        results = []
        for file_path in file_paths:
            result = self.store(file_path)
            results.append(result)
        return results
