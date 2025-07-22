import asyncio
from aiokafka import AIOKafkaConsumer
import aiohttp

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.example.com') as resp:
            return await resp.text()

def blocking_db_op():
    # Simulate sync DB call (e.g., psycopg2)
    import time; time.sleep(2)
    return "db_result"

async def scenario():
    # Step 1: Async HTTP
    data = await fetch_data()
    # Step 2: Await async Kafka event
    # ... (your aiokafka logic here)
    # Step 3: Sync DB op offloaded
    result = await asyncio.to_thread(blocking_db_op)
    return result

async def main():
    # Many concurrent combinatorial scenarios
    results = await asyncio.gather(*(scenario() for _ in range(100)))

asyncio.run(main())
