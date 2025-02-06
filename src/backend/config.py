# src/backend/config.py
import os

from dotenv import load_dotenv

# 加載 .env 檔案（如果存在）
load_dotenv()

# 向量資料庫（Milvus）配置
VECTOR_DB_HOST = os.getenv("VECTOR_DB_HOST", "localhost")
VECTOR_DB_PORT = int(os.getenv("VECTOR_DB_PORT", "19530"))

# Ollama LLM 配置
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-r1:3b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", "0.3"))

# 其他配置（可擴充）
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "200"))  # 文本切割大小
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "20"))  # 文本切割重疊
