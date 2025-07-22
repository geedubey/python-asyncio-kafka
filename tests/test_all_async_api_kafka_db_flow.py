import pytest
import asyncio
import json

@pytest.mark.asyncio
@pytest.mark.parametrize("input_data", json.load(open("tests/testdata/api_tests.json")))
async def test_api_kafka_db_flow(input_data, http_client, kafka_producer, kafka_consumer, db_conn):
    # 1. Send async HTTP request
    resp = await http_client.post("/api/do", json=input_data["api_input"])
    assert resp.status_code == 200

    # 2. Produce to Kafka
    await kafka_producer.send_and_wait("testtopic", b"testmsg")

    # 3. Consume from Kafka
    msg = await kafka_consumer.getone()
    assert msg.value == b"expected"

    # 4. Query database (async)
    row = await db_conn.fetchrow("SELECT * FROM sometable WHERE key=$1", input_data["db_key"])
    assert row is not None
# Test for API + Kafka + DB flow
