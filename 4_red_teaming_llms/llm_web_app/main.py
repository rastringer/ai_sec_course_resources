from fastapi import FastAPI, Request, Form, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import asyncio
from typing import List, Dict
import uuid
import json

app = FastAPI(title="LLM Chat with HTMX")
templates = Jinja2Templates(directory="templates")

# Store conversations in memory 
conversations: Dict[str, List[Dict]] = {}

# Default system message 
DEFAULT_SYSTEM_MESSAGE = "You are a helpful AI assistant. Be concise, accurate, and friendly. If you don't know something, admit it clearly."

def get_or_create_conversation(session_id: str) -> List[Dict]:
    """Get existing conversation or create new one with system message"""
    if session_id not in conversations:
        conversations[session_id] = [
            {
                "role": "system",
                "content": DEFAULT_SYSTEM_MESSAGE
            }
        ]
    return conversations[session_id]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    session_id = str(uuid.uuid4())
    return templates.TemplateResponse("index.html", {
        "request": request,
        "session_id": session_id,
        "default_system_message": DEFAULT_SYSTEM_MESSAGE  # Pass to template
    })

@app.post("/chat")
async def chat(
    request: Request,
    message: str = Form(...),
    session_id: str = Form(...),
    model: str = Form(default="orca-mini:3b"),
    system_prompt: str = Form(default=DEFAULT_SYSTEM_MESSAGE)  # Add system_prompt back
):
    """Handle chat message and return new message elements"""
    
    if not message.strip():
        return HTMLResponse("")
    
    # Get conversation history
    conversation = get_or_create_conversation(session_id)
    
    # Update system message if it changed
    if conversation[0]["role"] == "system":
        conversation[0]["content"] = system_prompt.strip() or DEFAULT_SYSTEM_MESSAGE
    
    # Add user message
    conversation.append({
        "role": "user",
        "content": message.strip()
    })
    
    # LOG THE MODEL AND SYSTEM MESSAGE
    print(f"🤖 Using model: {model}")
    print(f"💭 System prompt: {system_prompt[:100]}..." if len(system_prompt) > 100 else f"💭 System prompt: {system_prompt}")
    print(f"👤 User ({session_id[:8]}): {message.strip()}")
    
    # Create user message HTML
    user_message_html = f"""
    <div class="message user" id="user-{len(conversation)}">
        <div class="message-avatar">👤</div>
        <div class="message-content">
            {message.strip()}
            <div class="message-time">{get_current_time()}</div>
        </div>
    </div>
    """
    
    # Create thinking indicator
    thinking_html = f"""
    <div class="message bot" id="thinking-indicator">
        <div class="message-avatar">🤖</div>
        <div class="message-content">
            <div class="typing-indicator">
                Thinking
                <div class="typing-dots">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        </div>
    </div>
    """
    
    try:
        # Call Ollama
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                "messages": conversation,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_k": 40,
                    "top_p": 0.9,
                }
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            bot_response = result["message"]["content"]
            
            # Add assistant response to conversation
            conversation.append({
                "role": "assistant",
                "content": bot_response
            })
            
            # LOG THE RESPONSE
            print(f"🤖 Bot response length: {len(bot_response)} characters")
            
        else:
            print(f"❌ Ollama error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    # Return both user message, thinking indicator, and trigger for bot response
    return HTMLResponse(
        user_message_html + thinking_html + 
        f'<div hx-get="/bot-response/{session_id}" hx-trigger="load delay:100ms" hx-swap="outerHTML"></div>'
    )

@app.get("/bot-response/{session_id}")
async def get_bot_response(session_id: str):
    """Get the latest bot response and remove thinking indicator"""
    conversation = conversations.get(session_id, [])
    
    if len(conversation) < 2:
        return HTMLResponse("")
    
    # Get the last assistant message
    last_message = conversation[-1]
    if last_message["role"] != "assistant":
        return HTMLResponse("")
    
    bot_response = last_message["content"]
    
    return HTMLResponse(f"""
    <script>
        document.getElementById('thinking-indicator')?.remove();
    </script>
    <div class="message bot" id="bot-{len(conversation)}">
        <div class="message-avatar">🤖</div>
        <div class="message-content">
            {bot_response.replace(chr(10), '<br>')}
            <div class="message-time">{get_current_time()}</div>
        </div>
    </div>
    """)

@app.post("/clear-chat")
async def clear_chat(session_id: str = Form(...), system_prompt: str = Form(default=DEFAULT_SYSTEM_MESSAGE)):
    """Clear chat history but keep the current system message"""
    if session_id in conversations:
        # Reset to just the system message (use current system prompt)
        conversations[session_id] = [
            {
                "role": "system",
                "content": system_prompt.strip() or DEFAULT_SYSTEM_MESSAGE
            }
        ]
    
    return HTMLResponse(f"""
    <div class="message bot">
        <div class="message-avatar">🤖</div>
        <div class="message-content">
            Chat cleared! How can I help you?
            <div class="message-time">{get_current_time()}</div>
        </div>
    </div>
    """)

@app.get("/health")
async def health_check():
    """Check if Ollama is running"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json()
            return {
                "status": "ok",
                "available_models": [model['name'] for model in models.get('models', [])]
            }
    except:
        return {"status": "error", "message": "Ollama not running"}

def get_current_time():
    """Get current time formatted for display"""
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)