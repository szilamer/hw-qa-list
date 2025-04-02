import streamlit as st
import json
import os
from pdf_qa_agent import PDFQAAgent
from pathlib import Path
import time
from fpdf import FPDF
import io
from dotenv import load_dotenv

# Környezeti változók betöltése
load_dotenv()

# Alapértelmezett modell betöltése környezeti változóból
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "o3-mini")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "8192"))

# Oldal konfigurálása
st.set_page_config(
    page_title="PDF QA Agent Frontend",
    page_icon="📚",
    layout="wide"
)

def main():
    st.title("📚 PDF QA Agent Frontend")
    
    # PDF fájl feltöltése
    uploaded_file = st.file_uploader("PDF fájl kiválasztása", type="pdf")
    
    if uploaded_file is not None:
        # TODO: Implement PDF processing
        pass

if __name__ == "__main__":
    main()