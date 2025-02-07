# src/vector_db/db_handler.py
from langchain_milvus import Milvus
from langchain_huggingface import HuggingFaceEmbeddings

from backend.config import VECTOR_DB_HOST, VECTOR_DB_PORT


def get_vector_db():
    embeddings = HuggingFaceEmbeddings(model_name="aspire/acge_text_embedding")

    connection_args = {"host": VECTOR_DB_HOST, "port": VECTOR_DB_PORT}
    vector_db = Milvus(
        collection_name="chatbot_collection",
        connection_args=connection_args,
        embedding_function=embeddings,
        auto_id=True
    )
    return vector_db
