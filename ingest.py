import pandas as pd
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
# Text splitter import: try both possible package locations (different langchain versions)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import os

csv_path = "data/medicine_dataset_with_stock.csv"  # 🔁 change this to your CSV filename
persist_directory = "chroma_db"

# ---- STEP 1: Load dataset ----
df = pd.read_csv(csv_path)

# ---- STEP 2: Convert each row into a descriptive text ----
docs = []
for _, row in df.iterrows():
    text = (
        f"Medicine Name: {row.get('Name', '')} | "
        f"Category: {row.get('Category', '')} | "
        f"Dosage Form: {row.get('Dosage Form', '')} | "
        f"Strength: {row.get('Strength', '')} | "
        f"Manufacturer: {row.get('Manufacturer', '')} | "
        f"Indication: {row.get('Indication', '')} | "
        f"Classification: {row.get('Classification', '')} | "
        f"Stock: {row.get('Stock', '')}"
    )
    docs.append(text)

print(f"✅ Loaded {len(docs)} medicines from {csv_path}")

# ---- STEP 3: Create embeddings and vectorstore ----
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_texts(docs, embedding=embeddings, persist_directory=persist_directory)
vectorstore.persist()

print(f"✅ Chroma vector database created and saved at '{persist_directory}'")