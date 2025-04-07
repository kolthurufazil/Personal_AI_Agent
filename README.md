# Multimodal AI Agent (Image + Text Q&A using Gemini Vision)

This project is an intelligent, multimodal AI agent that allows users to upload an image (such as a screenshot, receipt, document, or code) and ask questions about its contents. Powered by Google's **Gemini Pro Vision**, the app extracts text from the image and generates context-aware responses.

---

## Features

- Upload any PNG or JPG image (screenshots, code, receipts, etc.)
- Personal AI agent analyzes both the image and your question
- Get intelligent, contextual answers from the extracted content
- API key and model name securely handled with `.env`
- Clean, minimal interface built with Streamlit

---

## Tech Stack

| Layer         | Tool                          |
|---------------|-------------------------------|
| Frontend      | Streamlit                     |
| Image Handling| Pillow (PIL)                  |
| AI Reasoning  | Google Gemini Pro Vision API  |
| API Security  | python-dotenv                 |

---

## Setup Instructions

### 1. Clone the repository

### 2. Create a virtual environment
- python -m venv .venv
- source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows

### 3. Install dependencies
- pip install -r requirements.txt

### 4. Create a .env file for API key
- In the root folder, create a file called api_key.env with the following:

- Gemini_API_key=your_actual_key_here
- GEMINI_MODEL=gemini-1.5-pro-latest

### 5. Run the App
- streamlit run app.py
- Upload an image, ask a question, and watch the AI agent respond
