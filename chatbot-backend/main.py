from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# --- Configuration ---
load_dotenv()  # Load environment variables from .env file

# Check if the API key is provided
if "GOOGLE_API_KEY" not in os.environ:
    raise EnvironmentError("GOOGLE_API_KEY environment variable is not set.")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Model Initialization ---
try:
    model = genai.GenerativeModel('gemini-2.0-flash')
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
        response = model.generate_content(chat_input.user_message)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating content: {e}")
