Download Ollama online

Install Needed Addons in Powershell
    pip install llama-index llama-index-llms-ollama llama-index-embeddings-huggingface sentence-transformers

Insert combined_documents.txt into .ollama file within the Documents folder

Place Modelfile and rag_demo.py into the models folder

In Powershell go into the models folder in .ollama 
    cd C:\Users\<INSERTUSERHERE>\.ollama\models

Run Python Script
    python rag_demo.py    

Test the chatbot and make sure you are getting a response if not something is wrong

Close the chatbot but remain in the models folder

Run in Powershell 
    ollama create muffin-hr -f Modelfile