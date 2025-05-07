import aiohttp, asyncio, json, os
from datetime import date

async def fetch_documents(session, start_date):
    url = f"https://www.federalregister.gov/api/v1/documents.json?conditions[publication_date][gte]={start_date}&order=newest"
    async with session.get(url) as response:
        return await response.json()

async def save_raw_data(data):
    os.makedirs("data/raw", exist_ok=True)
    filename = f"data/raw/{date.today()}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

async def run():
    async with aiohttp.ClientSession() as session:
        data = await fetch_documents(session, "2025-04-01")
        await save_raw_data(data)

if __name__ == "__main__":
    asyncio.run(run())