Download Ollama online

Install Needed Addons in Powershell
    pip install llama-index llama-index-llms-ollama llama-index-embeddings-huggingface sentence-transformers

Insert combined_documents.txt into .ollama file within the Documents folder
    "C:\Users\<INSERTUSERHERE>\.ollama\models\documents"

Place Modelfile and rag_demo.py into the models folder

Open rag_demo.py and change line 8 to
    combined_file = r"C:\Users\<INSERTUSERHERE>\.ollama\models\documents\combined_documents.txt"

In Powershell go into the models folder in .ollama 
    cd C:\Users\<INSERTUSERHERE>\.ollama\models

Run Python Script
    python rag_demo.py    

Test the chatbot and make sure you are getting a response if not something is wrong

Close the chatbot but remain in the models folder

Run in Powershell 
    ollama create muffin-hr -f Modelfile

Run command to see if you can see the model 
    ollama list

If you see the list with the muffin-hr then you have completed everything in command prompt and Powershell

On the Ollama application you will need to go into the settings and for model location you will need to set it to 
    "C:\Users\<INSERTUSERHERE>\.ollama\models\manifests\registry.ollama.ai\library\muffin-hr"

On the main page on the bottom corner drop the menu and look untill you find muffin-hr
