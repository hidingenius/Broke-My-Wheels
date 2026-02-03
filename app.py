import gradio as gr
from ollama import Client

MODEL = "llama3.2:3b"  # small/fast; upgrade to llama3.1:8b for detailed schematics
client = Client()     # Assumes Ollama running locally

# Load system prompt
with open("system_prompt.txt", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

def bmw_chat(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        if assistant_msg:
            messages.append({"role": "assistant", "content": assistant_msg})
    
    messages.append({"role": "user", "content": message})
    
    response = ""
    stream = client.chat(
        model=MODEL,
        messages=messages,
        stream=True,
    )
    
    for chunk in stream:
        content = chunk['message']['content']
        response += content
        yield response

demo = gr.ChatInterface(
    fn=bmw_chat,
    title="BMW Build AI",
    description=(
        "Guten Tag! I am Fritz, your BMW tuner. "
        "Ask about mods for 80s M3 E30 or E46 328/330 — balanced for performance & style. Schematics too!"
    ),
    examples=[
        "Suggest balanced mods for a 1987 BMW M3 E30.",
        "Build plan for E46 330 with aesthetics and handling focus.",
        "Generate schematic for brake upgrade on 328.",
        "Wheel options for M3 that improve grip and looks.",
    ],
    cache_examples=False,
)

if __name__ == "__main__":
    demo.launch()
