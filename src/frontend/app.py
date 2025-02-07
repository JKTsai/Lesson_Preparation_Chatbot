import gradio as gr
import requests
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from backend.pdf_processor import PDFProcessor

pdf_processor = PDFProcessor()
chat_history = []  # 存儲對話記錄

def upload_and_process(files):
    """處理多個 PDF 文件"""
    file_paths = [file.name for file in files]
    results = pdf_processor.process_multiple_pdfs(file_paths)
    formatted_results = [
        f"<span style='color: green; font-weight: bold;'>&#10003; {result}</span>"
        for result in results
    ]
    return "<br>".join(formatted_results)

def ask_chatbot(history, user_input):
    """調用 FastAPI 來回答問題，並保存聊天歷史"""
    try:
        response = requests.post("http://localhost:8000/query/", params={"question": user_input})
        if response.status_code == 200:
            data = response.json()
            bot_response = data.get("answer", "未收到回答")
        else:
            bot_response = f"錯誤：{response.status_code} - {response.text}"
    except Exception as e:
        bot_response = f"請求失敗：{e}"

    # 更新聊天歷史記錄
    history.append((user_input, bot_response))
    return history, ""  # 返回更新後的聊天記錄，並清空輸入框

with gr.Blocks() as demo:
    gr.Markdown("""
    # 📚 鄭老師的備課GPT(效果不好請回饋給開發者)
    """)

    with gr.Tab("📂 上傳 PDF"):
        file_input = gr.File(label="📎 上傳 PDF 文件", file_count="multiple", file_types=[".pdf"])
        upload_button = gr.Button("Upload")
        output_text = gr.HTML(label="Results")
        upload_button.click(upload_and_process, inputs=file_input, outputs=output_text)

    with gr.Tab("💬 問問題"):
        chatbot = gr.Chatbot(label="Chatbot 對話")  # 記錄對話歷史
        user_input = gr.Textbox(label="輸入你的問題")
        ask_button = gr.Button("Enter")
        
        ask_button.click(ask_chatbot, inputs=[chatbot, user_input], outputs=[chatbot, user_input])

if __name__ == "__main__":
    demo.launch()