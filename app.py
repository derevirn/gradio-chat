import gradio as gr
import ollama

def chat(message, history):
    messages = [{"role": "user", "content": message}]
    response = ollama.chat(
        model="qwen3",  # Replace with your model
        messages=messages,
        think=False  # Disables thinking for faster responses
    )
    return response["message"]["content"]

demo = gr.ChatInterface(
    chat,
    title="Ollama Chat"
)

if __name__ == "__main__":
    demo.launch()
