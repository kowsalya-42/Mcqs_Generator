MCQ_PROMPT_TEMPLATE = """
You are an AI that creates new, unique MCQs in the following strict format:

@title {title}
@description {description}

{questions_block}

Rules:
- Create completely new questions inspired by the given content — change the numbers, wording, and context so it's not identical to the input.
- The question should be the same type (same topic & difficulty) but **must not reuse the same numbers or sentences**.
- Use EXACT formatting with @title, @description, @question, @instruction, @difficulty, @Order, @option, @@option (for correct one), @explanation, @subject, @unit, @topic, @plusmarks.
- Difficulty should be one of: easy, moderate, hard.
- Subject, unit, and topic must be chosen from the given curriculum:
{curriculum}
- Ensure questions are diverse and cover different cognitive levels.
- Do not include any extra text outside the required format.

Content to base new questions on:
{text_content}
"""
