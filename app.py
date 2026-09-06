import os
import subprocess
import time
import requests
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough


# ---- Helper: Check if Ollama is running ----
def is_ollama_running():
    try:
        r = requests.get("http://127.0.0.1:11434/api/tags", timeout=3)
        return r.status_code == 200
    except requests.exceptions.RequestException:
        return False


# ---- Helper: Start Ollama if not running ----
def start_ollama():
    if is_ollama_running():
        print("✅ Ollama is already running.")
        return
    print("🚀 Starting Ollama in CPU mode...")
    os.environ["OLLAMA_NO_GPU"] = "true"
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("🕐 Waiting for Ollama to start...")
    for _ in range(25):
        if is_ollama_running():
            print("✅ Ollama is now running!")
            return
        time.sleep(1)
    raise RuntimeError("❌ Ollama failed to start within 25 seconds.")


# ---- Ensure Ollama is running ----
start_ollama()


# ---- Load vector store ----
persist_directory = "chroma_db"
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})


# ---- Try loading model with fallback ----
def load_model():
    """Try smaller models automatically if memory fails."""
    preferred_models = ["tinyllama","phi3:mini", "llama3.2:1b", "llama3.1:latest"]

    for model_name in preferred_models:
        try:
            print(f"🧠 Trying to load model: {model_name} ...")
            llm = ChatOllama(model=model_name, temperature=0.2)
            llm.invoke("Hello")
            print(f"✅ Model '{model_name}' loaded successfully!\n")
            return llm
        except Exception as e:
            print(f"⚠️ Model '{model_name}' failed due to: {e}\nTrying next model...\n")
    raise RuntimeError("❌ No suitable model could be loaded.")


llm = load_model()


# ---- Improved Prompt Template ----
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "You are a smart, caring, and accurate **Medical Assistant AI** that helps users with "
        "medical-related questions such as symptoms, treatments, medicines, and first aid.\n\n"
        "Below is the information retrieved from the medical database. It may include medicine names, "
        "their use cases, dosage forms, strengths, manufacturers, classifications, and stock availability.\n\n"
        "If the user’s question relates to any medicine or health condition mentioned in the context, "
        "summarize and present all relevant medicine details clearly and neatly. If stock information is available, include it.\n\n"
        "If the context does not contain relevant details, give a general medical explanation using real-world knowledge, "
        "and politely recommend consulting a healthcare professional if symptoms persist.\n\n"
        "🧠 **Context (medical database summary):**\n{context}\n\n"
        "💬 **User Question:** {question}\n\n"
        "✅ **Helpful and medically accurate answer:**"
    ),
)


# ---- Format documents properly ----
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


# ---- Updated RAG chain ----
rag_chain = (
    RunnableParallel({"context": retriever | format_docs, "question": RunnablePassthrough()})
    | prompt
    | llm
    | StrOutputParser()
)


# ---- Console Interaction ----
if __name__ == "__main__":
    print("\n🩺 Medical Agent ready! Type your question below.\n")
    while True:
        q = input("💬 Ask something (or type 'exit'): ")
        if q.lower().strip() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        try:
            answer = rag_chain.invoke(q)
            print("\n🤖", answer, "\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
