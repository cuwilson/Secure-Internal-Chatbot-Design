
import os
from llama_index.core import VectorStoreIndex, Document
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Path to your combined text file
combined_file = r"C:\Users\ncole\.ollama\models\documents\combined_documents.txt"

# Check if file exists
if not os.path.exists(combined_file):
    raise FileNotFoundError(f"File not found: {combined_file}")

# Read the file content
with open(combined_file, "r", encoding="utf-8") as f:
    text_content = f.read()

# Create Document object correctly
documents = [Document(text=text_content)]

# Embedding model
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Build index
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Connect to Ollama
llm = Ollama(model="llama3")
query_engine = index.as_query_engine(llm=llm)

print("Muffin Maniacs HR Assistant! What can I help you with today? (type 'exit' to quit):")
while True:
    user_q = input("You: ")
    if user_q.lower() in ["exit", "quit"]:
        break
    response = query_engine.query(user_q)
    print("Answer:", response)
