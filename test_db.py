from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

persist_directory = "chroma_db"
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

print("Documents in DB:", vectorstore._collection.count())
