# src/backend/rag_pipeline.py
import sys

from config import OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_TEMPERATURE
from langchain_ollama import ChatOllama

from vector_db.db_handler import get_vector_db


class RAGPipeline:
    def __init__(self):
        """
        initialize RAG Pipeline：
        - set up LLM
        - connect to DB
        """
        self.llm = ChatOllama(
            model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, temperature=OLLAMA_TEMPERATURE
        )
        self.vector_db = get_vector_db()

    def retrieve_context(self, question: str, k: int = 3) -> str:
        """
        retrieval from vector DB
        """
        docs = self.vector_db.similarity_search(question, k=k)
        return "\n".join([doc.page_content for doc in docs])

    def generate_answer(self, question: str) -> str:
        """
        generate response using retrieved data
        """
        context = self.retrieve_context(question)
        prompt = f"根據以下內容回答問題：\n{context}\n\n問題：{question}"
        response = self.llm.invoke([("human", prompt)])
        return response.content


# 創建一個全域的 RAGPipeline 實例
rag_pipeline = RAGPipeline()
