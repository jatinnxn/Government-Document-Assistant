# US Government Document Assistant

An AI-powered assistant that answers questions based on official US government documents. It uses a Retrieval-Augmented Generation (RAG) pipeline with MySQL and the Federal Register API, integrated with a local Mistral LLM (via Ollama) to generate accurate, context-aware responses. The interface is built using Streamlit.

## Features

- *Natural Language Question Answering* on US executive documents.
- *Context Retrieval from MySQL* and *Federal Register API* as fallback.
- *LLM Response Generation* via ollama run mistral subprocess.
- *Streamlit Web Interface* for interactive Q&A.
- *Unicode and memory-safe* processing for seamless use.

## Tech Stack

- *Python*  
- *MySQL*  
- *Ollama* (Local Mistral model)  
- *Streamlit*  
- *Federal Register API*

## Installation

1. *Clone the repository*
   bash
   git clone https://github.com/your-username/us-doc-assistant.git
   cd us-doc-assistant

2.	Install dependencies

pip install -r requirements.txt


3.	Start MySQL and import your data to jatinidb1 (or update tools.py to match your DB settings).
4.	Run Streamlit UI
    streamlit run data_pipeline/ui.py



5.  Requirements
	•	Python 3.10+
	•	MySQL Server
	•	Ollama installed with mistral or gemma:2b model
	•	Internet access (for API fallback)

 6.  Folder Structure

data_pipeline/

    agent.py               # Core LLM query logic
    downloader.py          # Document downloader
    processor.py           # Data formatting (if needed)
    tools.py               # MySQL + API fetch functions
    ui.py                  # Streamlit app
    main.py                # Optional CLI interface
    2025-05-07.json        # Sample data (if any)

 7.  Sample Usage
     Ask questions like:
	    •	What did the president publish on 2025-05-07?
	    •	Tell me about the Religious Liberty Commission executive order.

 8.  Credits:
      Built by Jatin Avhad as part of an AI/ML academic project.

### Bonus: `requirements.txt`

          txt
          pymysql
          requests
          streamlit
