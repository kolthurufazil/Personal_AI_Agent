import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Load API key and model name from .env
load_dotenv("api_key.env")
genai.configure(api_key=os.getenv("Gemini_API_key"))
model_name = os.getenv("GEMINI_MODEL")

# Extract info from image using Gemini Vision
def image_analysis(image_path, question):
    model = genai.GenerativeModel(model_name)
    image = Image.open(image_path)
    response = model.generate_content([question, image])
    return response.text.strip()
