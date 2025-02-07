# src/backend/config.py
import os

from dotenv import load_dotenv

# 加載 .env 檔案（如果存在）
load_dotenv()

# 向量資料庫（Milvus）配置
VECTOR_DB_HOST = os.getenv("VECTOR_DB_HOST", "localhost")
VECTOR_DB_PORT = int(os.getenv("VECTOR_DB_PORT", "19530"))

# LLM
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.3"))


# 其他配置（可擴充）
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "200"))  # 文本切割大小
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "20"))  # 文本切割重疊
