import google.generativeai as genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key="AQ.Ab8RN6KHeDcPo7Tb4RnC_z7xueIhmD1J30q47a0BKWbVdyGx_Q")


class PromptRequest(BaseModel):
  prompt: str


@app.post("/generate")
def generate_response(request: PromptRequest):
  try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(request.prompt)
    return {"response": response.text}
  except Exception as e:
    return {"error": str(e)}