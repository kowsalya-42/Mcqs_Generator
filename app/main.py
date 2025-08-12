from fastapi import FastAPI
from .routes import router

app = FastAPI(title="MCQ Generator LLM API")
app.include_router(router)

@app.get("/")
def home():
    return {"message": "MCQ Generator API is running. Visit /docs to test."}
