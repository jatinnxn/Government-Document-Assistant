import subprocess
import sys
from tools import fetch_documents_from_db


sys.stdout.reconfigure(encoding='utf-8')

def query_llm(prompt):
    
    result = subprocess.run(
        ["ollama", "run", "gemma:2b", prompt],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return result.stdout.strip()

def generate_answer(user_query):
    
    documents = fetch_documents_from_db(user_query)

    if not documents:
        return "No relevant documents found for your query."

    
    context = "\n\n".join([
        f"Title: {doc['title']}\nDate: {doc['date']}\nPresident: {doc['president']}\nSummary: {doc['summary']}"
        for doc in documents[:5]  
    ])

    
    prompt = f"""You are a government policy assistant.
Answer the following user question using only the documents provided below:

Documents:
{context}

Question: {user_query}
Answer:"""

    
    return query_llm(prompt)


if __name__ == "__main__":
    question = input("Ask me about US government documents: ")
    print("\n" + generate_answer(question))