from openai import OpenAI
from .config import OPENAI_API_KEY
from .prompt_template import MCQ_PROMPT_TEMPLATE  # import your template
import json

client = OpenAI(api_key="key")

def generate_mcqs(text_content, title, description):
    # Load curriculum JSON
    with open("app/curriculum.json") as f:
        curriculum = json.dumps(json.load(f), indent=2)

    # Fill in the template
    prompt = MCQ_PROMPT_TEMPLATE.format(
        title=title,
        description=description,
        questions_block="",  # LLM generates this
        curriculum=curriculum,
        text_content=text_content
    )

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",  # or gpt-4-turbo
        messages=[
            {"role": "system", "content": "You are an AI that generates MCQs in a strict format."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
