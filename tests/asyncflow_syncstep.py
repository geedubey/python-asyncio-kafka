import asyncio
from aiokafka import AIOKafkaConsumer
import requests  # sync HTTP client
import psycopg2   # sync DB client

async def handle_kafka_message(msg):
    # Sync HTTP request in async context (blocking! not scalable)
    response = requests.post('https://api.example.com/endpoint', data={'value': msg.value})
    # You could offload:
    # response = await asyncio.to_thread(requests.post, 'https://api...', data={...})
    # Sync DB write
    conn = psycopg2.connect(...)
    cur = conn.cursor()
    cur.execute('INSERT INTO ...', ...)
    conn.commit()
    cur.close()
    conn.close()

async def consume():
    consumer = AIOKafkaConsumer("topic", bootstrap_servers="localhost:9092")
    await consumer.start()
    try:
        async for msg in consumer:
            await handle_kafka_message(msg)
    finally:
        await consumer.stop()

asyncio.run(consume())
