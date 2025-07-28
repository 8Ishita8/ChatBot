from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess
from better_profanity import profanity

app = FastAPI()

profanity.load_censor_words()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    original_message = msg.message.strip()
    censored_message = profanity.censor(original_message)  

   
    if profanity.contains_profanity(original_message):
        return {
            "user_message": censored_message,
            "response": "🧸 Hey! Let's keep things sweet and respectful ❤️"
        }

    
    prompt = f"<s>[INST] {original_message} [/INST]"

    try:
        process = subprocess.Popen(
            ["ollama", "run", "mistral:7b-instruct"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )

        output, error = process.communicate(input=prompt, timeout=60)

        if process.returncode != 0:
            return {
                "user_message": censored_message,
                "response": f"Model error: {error.strip()}"
            }

        return {
            "user_message": censored_message,
            "response": output.strip()
        }

    except Exception as e:
        return {
            "user_message": censored_message,
            "response": f"Error: {str(e)}"
        }
