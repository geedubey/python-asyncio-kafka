# Kafka-related pytest fixtures

import pytest
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

KAFKA_BOOTSTRAP = 'localhost:9092'
TOPIC = 'kontext-events'


@pytest.fixture
async def kafka_producer():
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP)
    await producer.start()
    yield producer
    await producer.stop()


@pytest.fixture
async def kafka_consumer():
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='pytest-group',
    )
    await consumer.start()
    yield consumer
    await consumer.stop()
