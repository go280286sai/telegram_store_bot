"""
Delivery route test
"""
import json

from httpx import AsyncClient, ASGITransport
from app.main import app
import pytest
import pytest_asyncio

transport = ASGITransport(app=app)


@pytest_asyncio.fixture
async def client():
    """
    Fixture fixture for test client function
    :return:
    """
    async with AsyncClient(
            transport=transport,
            base_url="http://test"
    ) as client:
        yield client


@pytest.mark.asyncio
async def test_delivery_create(client: AsyncClient):
    """
    Test delivery creates route
    :param client:
    :return:
    """
    response = await client.post("/deliveries/create",
                                 json={
                                     "name": "Name",
                                     "description": "Description"
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_delivery_get_one(client: AsyncClient):
    """
    Test delivery get one route
    :param client:
    :return:
    """
    response = await client.get("/deliveries/get/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"]["name"] == "Name"
    assert obj["data"]["description"] == "Description"
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_delivery_update(client: AsyncClient):
    """
    Test delivery update route
    :param client:
    :return:
    """
    response = await client.post("/deliveries/update/1",
                                 json={
                                     "name": "Name1",
                                     "description": "Description1"
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_deliveries_get_all(client: AsyncClient):
    """
    Test deliveries get all routes
    :param client:
    :return:
    """
    response = await client.get("/deliveries/")
    assert response.status_code == 200
    objs = json.loads(response.text)
    assert objs["success"] is True
    for obj in objs["data"]["deliveries"]:
        assert obj["name"] == "Name1"
        assert obj["description"] == "Description1"
    assert objs["error"] is False


@pytest.mark.asyncio
async def test_delivery_delete(client: AsyncClient):
    """
    Test delivery delete route
    :param client:
    :return:
    """
    response = await client.post("/deliveries/delete/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False
