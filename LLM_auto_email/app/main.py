from fastapi import FastAPI, HTTPException, Header, Depends
from app.schemas import EmailDraftRequest
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_AUTH_KEY = os.getenv("API_AUTH_KEY")  # optional

client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI(title="Personalized Email Drafting Assistant")

# Optional API Key Authentication
def verify_api_key(x_api_key: str = Header(...)):
    if API_AUTH_KEY and x_api_key != API_AUTH_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.post("/generate")
def generate_email(
    request: EmailDraftRequest,
    api_key: None = Depends(verify_api_key) if API_AUTH_KEY else None
):
    prompt = (
        f"Compose an email with the following details:\n\n"
        f"To: {request.to}\n"
        f"From: {request.from_}\n"
        f"Title: {request.title}\n"
        f"Body Context: {request.body}\n\n"
        f"Generate a clear and professional draft."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful email drafting assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5
        )
        draft_text = response.choices[0].message.content.strip()
        return {"draft": draft_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
