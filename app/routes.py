from fastapi import APIRouter, UploadFile, Form
from .llm_service import generate_mcqs
from .ocr_service import extract_text_from_image

router = APIRouter()

@router.post("/generate_mcqs")
async def create_mcqs(
    file: UploadFile = None,
    text: str = Form(None),
    title: str = Form(...),
    description: str = Form(...)
):
    if file:
        file_bytes = await file.read()
        text_content = extract_text_from_image(file_bytes)
    else:
        text_content = text

    mcq_output = generate_mcqs(text_content, title, description)
    return {"mcq_output": mcq_output}
