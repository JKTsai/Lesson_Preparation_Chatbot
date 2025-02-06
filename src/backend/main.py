# src/backend/main.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# print("🔍 Python 搜索路徑")
# for path in sys.path:
#     print(path)
import uvicorn
from fastapi import FastAPI
from rag_pipeline import rag_pipeline

app = FastAPI(title="Ollama RAG Chatbot API")


@app.get("/")
async def root():
    return {"message": "Welcome to the Ollama RAG Chatbot API"}


@app.post("/query/")
async def query(question: str):
    answer = rag_pipeline.generate_answer(question)
    return {"answer": answer}


if __name__ == "__main__":
    # 使用 reload=True 可在開發時自動重啟
    uvicorn.run("src.backend.main:app", host="0.0.0.0", port=8000, reload=True)
