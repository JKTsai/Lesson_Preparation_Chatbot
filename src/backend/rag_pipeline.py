import sys
from config import OPENAI_MODEL, OPENAI_TEMPERATURE
from langchain_openai import ChatOpenAI
from vector_db.db_handler import get_vector_db

class RAGPipeline:
    def __init__(self):
        """
        初始化 RAG Pipeline：
        - 設定 LLM
        - 連接向量資料庫
        - 建立聊天歷史記錄
        """
        self.llm = ChatOpenAI(
            model=OPENAI_MODEL,
            temperature=OPENAI_TEMPERATURE,
        )
        self.vector_db = get_vector_db()
        self.chat_history = []  # 記錄歷史對話

    def retrieve_context(self, question: str, k: int = 3) -> str:
        """
        從向量資料庫檢索與問題最相關的文本
        """
        docs = self.vector_db.similarity_search(question, k=k)
        return "\n".join([doc.page_content for doc in docs])

    def generate_answer(self, question: str) -> str:
        """
        產生回應，並將歷史聊天記錄與新問題一起傳給 LLM
        """
        context = self.retrieve_context(question)
        
        # 構建完整的聊天歷史與新問題
        chat_messages = self.chat_history + [("human", f"根據以下內容回答問題：\n{context}\n\n問題：{question}")]
        
        # 呼叫 LLM
        response = self.llm.invoke(chat_messages)
        
        # 更新聊天記錄（只保留最近 10 則對話，防止無限增長）
        self.chat_history.append(("human", question))
        self.chat_history.append(("ai", response.content))
        self.chat_history = self.chat_history[-10:]

        return response.content

# 創建全域的 RAGPipeline 實例
rag_pipeline = RAGPipeline()