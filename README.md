# MCQ Generator LLM

## Overview

The MCQ Generator LLM project provides an intelligent system for automated multiple-choice question (MCQ) generation utilizing large language models (LLMs). The backend is developed using FastAPI and integrates with OpenAI’s API to generate questions from textual and image inputs. The system also supports OCR-based text extraction to process images, allowing versatile input methods for educators and content creators.

## Project Architecture

The project follows a modular architecture, separating concerns between the backend API and the frontend client:

- **Backend (`app/`):**  
  - Implements RESTful API endpoints with FastAPI for MCQ generation.  
  - Handles LLM interactions with OpenAI’s API via a dedicated service layer.  
  - Processes images for text extraction using OCR.  
  - Uses a structured curriculum mapping (`curriculum.json`) to contextualize MCQ generation.  

- **Frontend (`frontend/`):**  
  - Python-based client application interfacing with the backend API to facilitate user interaction and MCQ generation workflows.

## Directory Structure

```
mcq_generator_llm/
├── app/
│   ├── init.py
│   ├── main.py                   # FastAPI application entry point
│   ├── config.py                 # Configuration management (API keys, settings)
│   ├── routes.py                 # API route definitions
│   ├── llm_service.py            # OpenAI API interaction and prompt management
│   ├── ocr_service.py            # OCR functionality for image-to-text conversion
│   ├── prompt_template.py        # LLM prompt templates for consistent question formatting
│   └── curriculum.json           # Curriculum hierarchy mapping for structured MCQ context
├── frontend/
│   └── main.py                   # Frontend client application
├── requirements.txt              # Python dependencies
└── README.md                    # Project documentation 
```


## Prerequisites

- Python 3.8 or higher  
- OpenAI API access and API key  
- Virtual environment tool (recommended)  

## Installation and Setup

1. **Clone the repository**

```bash
git clone https://github.com/kowsalya-42/Mcqs_Generator.git
cd mcq_generator_llm
```


2.**Create and activate a virtual environment**

```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3.**Install project dependencies**

```
pip install -r requirements.txt
```

4.**Configure API keys**

Set your OpenAI API key in app/config.py or as an environment variable as per your security preference.

5.**Run the backend server**

```uvicorn app.main:app --reload```


6.**Run the frontend client (in a separate terminal)**
```
python frontend/main.py
```
Access the application

Open your web browser and navigate to the frontend client URL (typically http://localhost:port) to begin generating MCQs.

7.**Usage**
Submit textual content via the frontend or upload images containing text.


## How It Works

- **Input Processing:**  
  Users submit math questions by typing text or uploading images containing questions.

- **Vectorization and Retrieval:**  
  The system extracts and breaks input text into chunks, computes embeddings, and stores them in a vector index. Relevant chunks are retrieved based on query similarity.

- **LLM Prompting and MCQ Generation:**  
  Retrieved content is formatted into prompts and sent to the LLM, which generates multiple-choice questions with options, explanations, and metadata.

- **Response Output:**  
  Generated MCQs are returned to the frontend for display and use.

- **Optional Follow-Up Logic:**  
  For ambiguous or incomplete input, the system may ask clarifying questions to refine the generated questions.

---

## 🧪 Example Use

**User Input:**  
```

The top view of a rectangular box contains 8 identical tightly packed spherical cans arranged in 2 rows of 4. Each can has a radius of 2 cm. Which of the following is closest to the dimensions (in cm) of the rectangular box?

(A) $4 \times 8 \times 8$  
(B) $4 \times 8 \times 16$  
(C) $8 \times 8 \times 16$  
(D) $8 \times 16 \times 16$  
(E) $8 \times 16 \times 24$
```

**System Output:**  

```
@title Sample Math Assessment  
@description Generated MCQs from input content  

@question If a rectangle has a length of 12 cm and a width of 8 cm, what is its area?  
@instruction Calculate the area of the rectangle using the given dimensions.  
@difficulty easy  
@Order 1  
@option 20 cm²  
@option 50 cm²  
@@option 96 cm²  
@option 160 cm²  
@explanation The area of a rectangle is found by multiplying its length by its width. Therefore, the area is 12 cm * 8 cm = 96 cm².  
@subject Quantitative Math  
@unit Geometry and Measurement  
@topic Area & Volume  
@plusmarks 1  
```

## Customization & Configuration
Modify the LLM endpoint or model configuration in prompt_template.py to change question style or model behavior.

Customize embedding models and vector databases (e.g., Chroma, FAISS, Qdrant) in store_index.py for retrieval performance and accuracy.

Update prompt templates or add domain-specific instructions to tailor MCQ generation for different subjects or difficulty levels.

Enable iterative prompt loops to allow follow-up questioning and refined MCQ generation, improving clarity and relevance.

## Disclaimer
This system is intended for educational and practice purposes only. Generated questions should be reviewed for accuracy before formal use in assessments or exams.

The backend extracts the relevant text and generates MCQs using the LLM.

Generated questions are contextualized using the curriculum mapping where applicable.

The frontend displays questions and answers interactively for review.


## Contributing
Contributions are welcome. Please fork the repository and submit a pull request with improvements or bug fixes. Ensure code adheres to the project’s style guidelines and includes appropriate tests.
