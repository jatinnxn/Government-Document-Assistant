import pymysql
import re
import requests

def extract_date_from_query(query):
    match = re.search(r'\d{4}-\d{2}-\d{2}', query)
    return match.group(0) if match else None

def fetch_documents_from_db(query):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Jatinavhad987565@",  
        database="jatindb1"
    )
    cursor = conn.cursor()

    keyword = query
    date_str = extract_date_from_query(query)

    query_sql = """
        SELECT title, publication_date, president, summary
        FROM executive_documents
        WHERE title LIKE %s OR summary LIKE %s OR president LIKE %s
    """
    values = [f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"]

    if date_str:
        query_sql += " OR publication_date = %s"
        values.append(date_str)

    cursor.execute(query_sql, values)
    results = cursor.fetchall()
    conn.close()

    documents = []
    for row in results:
        documents.append({
            "title": row[0],
            "date": str(row[1]),
            "president": row[2] if row[2] else "Unknown",
            "summary": row[3] if row[3] else "No summary provided."
        })

    if documents:
        return documents
    else:
        return fetch_documents_from_api(query)

def fetch_documents_from_api(query):
    base_url = "https://www.federalregister.gov/api/v1/documents.json"
    params = {"per_page": 5, "order": "newest", "conditions[term]": query}

    response = requests.get(base_url, params=params)
    response.encoding = 'utf-8'  

    if response.status_code != 200:
        return []

    data = response.json()
    documents = []
    for item in data.get("results", []):
        documents.append({
            "title": item.get("title", "No Title"),
            "date": item.get("publication_date", "Unknown"),
            "president": item.get("agencies", [{}])[0].get("name", "Unknown"),
            "summary": item.get("abstract", "No summary provided.")
        })

    return documents