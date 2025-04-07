import streamlit as st
import tempfile
from vision_engine import image_analysis

st.set_page_config(page_title="Multimodal Personal AI Agent", layout="centered")
st.title("📸 Upload Any Image and Ask Your Personal AI Agent")

# Image uploader
uploaded_file = st.file_uploader("Upload an image (JPG, PNG)", type=["jpg", "jpeg", "png"])

# Question input
question = st.text_input("What do you want to know from this image?")

# Process
if uploaded_file and question:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    with st.spinner("Your Personal AI agent is analyzing image..."):
        try:
            answer = image_analysis(temp_path, question)
            st.markdown(" AI agent Response:")
            st.write(answer)
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
