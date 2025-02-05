# 🧠 Ollama RAG Chatbot

This project is a **Retrieval-Augmented Generation (RAG) chatbot** powered by **LangChain, Milvus, and Ollama**.  
Users can upload PDF files, and the system will **extract, chunk, and store the data into Milvus**, allowing the chatbot to retrieve relevant context before generating responses using **DeepSeek-R1**.

---

## 🚀 **How to Run the Project**

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- **Python 3.10+**
- **Docker & Docker Compose**
- **Milvus (Vector Database)**
- **Ollama (for local LLM inference)**

You can check installations with:
```sh
python --version
docker --version
```
---
### **2️⃣ Start Milvus (Vector Database)**
Milvus is essential for storing vectorized document chunks.  
If **Milvus is not running**, you will get errors like:

pymilvus.exceptions.MilvusException: Failed to connect to Milvus

#### 👉 Start Milvus using Docker
If using Docker, run:
```sh
docker-compose -f docker/docker-compose.yml up –build
```
OR start Milvus as a standalone container:
```sh
docker run -d –name milvus 
-p 19530:19530 
milvusdb/milvus:latest
```

#### 🔍 Verify Milvus is Running
After starting Milvus, check its status:
```sh
docker ps
```
You should see a container named **milvus** running on **port 19530**.

---

### 3️⃣ Start the FastAPI Backend
Once Milvus is running, start the backend API:
```sh
cd src/backend
uvicorn main:app –host 0.0.0.0 –port 8000 –reload
```

Now, FastAPI should be accessible at:
http://localhost:8000

---

### 4️⃣ Start the Gradio Frontend
Run the following command to launch the **Gradio UI**:
```sh
cd src/frontend
python app.py
```
This will start the UI at:
http://127.0.0.1:7860