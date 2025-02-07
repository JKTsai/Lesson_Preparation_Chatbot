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
import logging
import traceback

logger = logging.getLogger("uvicorn.error")
app = FastAPI(title="RAG Chatbot API")


@app.get("/")
async def root():
    return {"message": "Welcome to the RAG Chatbot API"}


@app.post("/query/")
async def query(question: str):
    try:
        answer = rag_pipeline.generate_answer(question)
        return {"answer": answer}
    except Exception as e:
        error_message = f"❌ 錯誤：{str(e)}"
        logger.error(error_message)
        traceback.print_exc()  # 這行會顯示完整錯誤訊息
        return {"error": error_message}


if __name__ == "__main__":
    # 使用 reload=True 可在開發時自動重啟
    uvicorn.run("src.backend.main:app", host="0.0.0.0", port=8000, reload=True)
