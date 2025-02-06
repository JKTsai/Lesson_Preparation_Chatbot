# src/vector_db/db_handler.py
from langchain_milvus import Milvus
from sentence_transformers import SentenceTransformer

from backend.config import VECTOR_DB_HOST, VECTOR_DB_PORT


def get_vector_db():
    embedding = SentenceTransformer("aspire/acge_text_embedding")

    connection_args = {"host": VECTOR_DB_HOST, "port": VECTOR_DB_PORT}
    vector_db = Milvus(
        collection_name="chatbot_collection",
        connection_args=connection_args,
        embedding_function=embedding,
    )
    return vector_db
