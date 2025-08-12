import pytesseract
from PIL import Image
import io

def extract_text_from_image(image_file):
    image = Image.open(io.BytesIO(image_file))
    text = pytesseract.image_to_string(image)
    return text.strip()
