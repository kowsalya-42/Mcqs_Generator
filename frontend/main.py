import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/generate_mcqs"

st.set_page_config(page_title="MCQ Generator", page_icon="📚", layout="wide")

st.title("📚 Math MCQ Generator")
st.write("Enter a question or upload an image, and get MCQs in your required format.")

title = st.text_input("Assessment Title", "Sample Math Assessment")
description = st.text_input("Assessment Description", "Generated MCQs from input content")
text_question = st.text_area("Enter Question Text", "")
uploaded_file = st.file_uploader("Or upload an image", type=["png", "jpg", "jpeg"])

# Optional: Uncomment below to input curriculum JSON string if your backend needs it
# curriculum_json_string = st.text_area("Enter Curriculum JSON", '{"subject": "Math", "grade": "10"}')

if st.button("Generate MCQs"):
    files = {}
    data = {
        "text_content": text_question,
        "title": title,
        "description": description,
        # "curriculum": curriculum_json_string,  # Uncomment if you add the curriculum input above
    }

    if uploaded_file:
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

    with st.spinner("Generating MCQs..."):
        try:
            response = requests.post(BACKEND_URL, data=data, files=files)
        except Exception as e:
            st.error(f"Request failed: {e}")
            st.stop()

    if response.status_code == 200:
        mcqs = response.json().get("mcq_output", "")
        st.success("MCQs generated successfully!")
        st.code(mcqs, language="text")
    else:
        st.error(f"Error: {response.text}")
