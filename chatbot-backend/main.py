from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# --- Configuration ---
load_dotenv()  # Load environment variables from .env file

# Check if the API key is provided
if "GOOGLE_API_KEY" not in os.environ:
    raise EnvironmentError("GOOGLE_API_KEY environment variable is not set.")

# --- Model Initialization ---
try:
    model = init_chat_model('google_genai:gemini-2.5-flash-lite')
except Exception as e:
    raise RuntimeError(f"Failed to initialize Gemini model: {e}") from e

# --- FastAPI App ---
app = FastAPI(title="AI Chatbot API", description="API for interacting with a Gemini chatbot.", version="1.0.0")

# --- CORS Configuration ---
origins = [
    "http://localhost:5173",  # Development frontend
    # Add your deployed frontend URL here (e.g., "https://your-deployed-app.com")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],  # Only allow necessary methods
    allow_headers=["*"],
)

# --- Data Models ---
class ChatInput(BaseModel):
    user_message: str

# --- API Endpoints ---
@app.get("/", tags=["Health"])
async def health_check():
    """
    Endpoint to check the API's health status.
    """
    return {"status": "ok"}

@app.post("/chat", tags=["Chat"])
async def chat(chat_input: ChatInput):
    """
    Endpoint for chatting with the AI model.
    """
    try:
        response = model.invoke(chat_input.user_message)
        return {"response": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating content: {e}")
    
if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

