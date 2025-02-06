# src/frontend/app.py
import gradio as gr
import requests

from backend.pdf_processor import PDFProcessor

pdf_processor = PDFProcessor()


def upload_and_process(files):
    """process multiple PDFs from UI"""
    file_paths = [file.name for file in files]
    results = pdf_processor.process_multiple_pdfs(file_paths)
    return "\n".join(results)


def ask_chatbot(question):
    """call API to answer user query"""
    try:
        response = requests.post(
            "http://localhost:8000/query/", params={"question": question}
        )
        if response.status_code == 200:
            data = response.json()
            return data.get("answer", "未收到回答")
        else:
            return f"錯誤：{response.status_code} - {response.text}"
    except Exception as e:
        return f"請求失敗：{e}"


with gr.Blocks() as demo:
    gr.Markdown("鄭老師的備課chatbot")

    with gr.Tab("上傳 PDF"):
        file_input = gr.File(
            label="上傳 PDF 文件", file_count="multiple", file_types=[".pdf"]
        )
        upload_button = gr.Button("Upload")
        output_text = gr.Textbox(label="Results")
        upload_button.click(upload_and_process, inputs=file_input, outputs=output_text)

    with gr.Tab("提问"):
        question_input = gr.Textbox(label="Enter Your Question")
        ask_button = gr.Button("Enter")
        answer_output = gr.Textbox(label="Response")
        ask_button.click(ask_chatbot, inputs=question_input, outputs=answer_output)

if __name__ == "__main__":
    demo.launch()
