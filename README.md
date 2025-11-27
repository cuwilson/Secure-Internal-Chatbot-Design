# Muffin Mate - Internal HR Chatbot

## Team Members
- Aden Osman
- Copper Wilson
- King Sambonge
- Nathaniel Davis

## Project Overview
**Muffin Mate** is a secure, in-house HR chatbot designed for Muffin Maniacs employees. It provides 24/7 access to company policies, benefits information, and HR guidance, helping reduce HR workload and prevent data leaks. The system leverages a Retrieval-Augmented Generation (RAG) architecture powered by Llama 3 and hosted using Ollama, ensuring that all sensitive information remains within the company’s network.

## Key Features
- Natural language processing for HR policy queries
- Fast retrieval of relevant HR documents (PDFs, SharePoint)

## Technologies Used
- Ollama
- Python
- Llama3 


# Setup Instructions for Running the Muffin HR Prototype

## 1. Download Ollama
Download Ollama from the official site:

https://ollama.com/



## 2. Install Required Python Packages
Run the following in PowerShell:

```
pip install llama-index llama-index-llms-ollama llama-index-embeddings-huggingface sentence-transformers
```
## 3. Move Project Files
Copy `Modelfile` and `rag_demo.py` into your `.ollama\models` folder. Typically found here: 
```
C:\Users\<INSERTUSERHERE>\.ollama\models
```
*make sure <INSERTUSERHERE> is the user you are using*

## 4. Create the Documents Folder
Inside the `.ollama\models` directory, create a folder named `documents` and add the `combined_documents.txt`

## 5. Update rag_demo.py
Open `rag_demo.py` and update line 8 to the appropriate directory from step 4
```
EX: 

From -
combined_file = r"C:\Users\<INSERTUSERHERE>\.ollama\models\documents\combined_documents.txt"


To - 
combined_file = r"C:\Users\coppe\.ollama\models\documents\combined_documents.txt"
```

## 6. Navigate to the Models Folder
Back in Powershell navidate to the directory from step 3 by typing 
```
cd C:\Users\<INSERTUSERHERE>\.ollama\models
```

*Do not forget to change the <INSERTUSERHERE> to the appropriate user*

## 7. Run the Python Script
Still in Powershell, run the RAG demo by typing the following 
```
python rag_demo.py
```

If the chatbot responds, great! 
You can keep ask your questions in the command prompt or continue to create a custom model within Ollama to ask the question. 



*Before continuing, close the model by typing `exit` or `Ctrl+C`*
## 8. Build the Custom Model
In Powershell run the following:
```
ollama create muffin-hr -f Modelfile
```

Verfiy the model exists by typing:
```
ollama list
```
You should see `muffin-hr` in the list. If you do you should be able to open the Ollama Desktop App and choose it from the dropdown on the bottom right of the app. If not, continue on to step 9

## 9. Configure the Ollama App
In the Ollama desktop application: 
1. Go to **Settings**
2. Set the model location to: 
```
C:\Users\<INSERTUSERHERE>\.ollama\models\manifests\registry.ollama.ai\library\muffin-hr
```
3. Go back to the main screen and open the model dropdown in the bottom right corner
4. Select `mufffin-hr`

