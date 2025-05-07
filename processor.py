import json, pymysql
from datetime import date

def process_and_insert():
    
    with open(f"data/raw/{date.today()}.json") as f:
        data = json.load(f).get("results", [])

    
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Jatinavhad987565@",
        database="jatindb1"
    )
    cursor = conn.cursor()

    
    for doc in data:
        doc_id = doc.get("document_number", "")
        title = doc.get("title", "")
        pub_date = doc.get("publication_date", "")
        summary = doc.get("abstract", "")
        
        
        president = "Unknown"
        if doc.get("agencies"):
            president = doc["agencies"][0].get("name", "Unknown")

        cursor.execute(
            "INSERT INTO executive_documents (document_id, title, publication_date, president, summary) VALUES (%s, %s, %s, %s, %s)",
            (doc_id, title, pub_date, president, summary)
        )

    conn.commit()
    conn.close()
    print("Data inserted successfully.")

if __name__ == "__main__":
    process_and_insert()