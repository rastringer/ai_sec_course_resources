
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import requests
import uvicorn

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>LLM Chat</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        #chat { height: 400px; border: 1px solid #ccc; overflow-y: auto; padding: 10px; margin-bottom: 10px; background: #f9f9f9; }
        #input { width: 70%; padding: 10px; }
        #send { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
        .message { margin: 10px 0; padding: 5px; }
        .user { color: blue; background: #e3f2fd; border-radius: 5px; }
        .bot { color: green; background: #f1f8e9; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>LLM Chat</h1>
    <div id="chat"></div>
    <input type="text" id="input" placeholder="Type your message...">
    <button id="send">Send</button>

    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");
        const chat = document.getElementById('chat');
        const input = document.getElementById('input');
        const send = document.getElementById('send');

        function addMessage(message, isUser) {
            const div = document.createElement('div');
            div.className = `message ${isUser ? 'user' : 'bot'}`;
            div.innerHTML = `<strong>${isUser ? 'You' : 'Bot'}:</strong> ${message}`;
            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
        }

        function sendMessage() {
            const message = input.value.trim();
            if (message) {
                addMessage(message, true);
                ws.send(message);
                input.value = '';
            }
        }

        ws.onmessage = function(event) {
            addMessage(event.data, false);
        };

        ws.onerror = function(error) {
            addMessage("Connection error. Make sure Ollama is running!", false);
        };

        send.addEventListener('click', sendMessage);
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') sendMessage();
        });
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html_content)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        try:
            message = await websocket.receive_text()
            print(f"Received: {message}")

            response = requests.post("http://localhost:11434/api/generate", 
                json={
                    "model": "orca-mini:3b",
                    "prompt": message,
                    "stream": False
                }, timeout=30)

            if response.status_code == 200:
                result = response.json()
                await websocket.send_text(result["response"])
            else:
                await websocket.send_text(f"Error: {response.status_code}")

        except Exception as e:
            await websocket.send_text(f"Error: {str(e)}")
            break

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
