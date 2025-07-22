# Test for Kafka only


import pytest
from tests.fixtures.kafka_fixtures import kafka_producer, kafka_consumer, TOPIC

MESSAGE = b'This is test from async io kafka '

@pytest.mark.asyncio
async def test_aiokafka_produce_consume(kafka_producer, kafka_consumer):
    producer = await anext(kafka_producer)
    consumer = await anext(kafka_consumer)

    # Produce a message
    await producer.send_and_wait('kontext-events', MESSAGE)

    # Consume the message
    async for msg in consumer:
        print(f"Received: {msg.value}")
        assert msg.value == MESSAGE
        break


