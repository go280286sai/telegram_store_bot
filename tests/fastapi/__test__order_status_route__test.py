"""
Order status route test
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
async def test_orders_status_create(client: AsyncClient):
    """
    Test orders status creates route
    :param client:
    :return:
    """
    response = await client.post("/order_statuses/create",
                                 json={"status": "Wait"})
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_orders_status_get_one(client: AsyncClient):
    """
    Test orders status get one route
    :param client:
    :return:
    """
    response = await client.get("/order_statuses/get/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"]["status"] == "Wait"
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_orders_status_update(client: AsyncClient):
    """
    Test orders status update route
    :param client:
    :return:
    """
    response = await client.post("/order_statuses/update/1",
                                 json={
                                     "status": "Done"
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_orders_status_get_all(client: AsyncClient):
    """
    Test orders status gets all routes
    :param client:
    :return:
    """
    response = await client.get("/order_statuses/")
    assert response.status_code == 200
    objs = json.loads(response.text)
    assert objs["success"] is True
    for obj in objs["data"]["orders"]:
        assert obj["status"] == "Done"
    assert objs["error"] is False


@pytest.mark.asyncio
async def test_orders_status_delete(client: AsyncClient):
    """
    Test orders status delete route
    :param client:
    :return:
    """
    response = await client.post("/order_statuses/delete/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False
