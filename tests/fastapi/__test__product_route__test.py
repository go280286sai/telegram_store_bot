"""
Product route test
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
async def test_product_create(client: AsyncClient):
    """
    Test product creates route
    :param client:
    :return:
    """
    response = await client.post("/products/create",
                                 json={
                                     "name": "Name",
                                     "description": "Description",
                                     "price": 10.2,
                                     "amount": 5,
                                     "is_service": 0
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_product_get_one(client: AsyncClient):
    """
    Test product get one route
    :param client:
    :return:
    """
    response = await client.get("/products/get/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"]["name"] == "Name"
    assert obj["data"]["description"] == "Description"
    assert obj["data"]["price"] == 10.2
    assert obj["data"]["amount"] == 5
    assert obj["data"]["is_service"] == 0
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_products_update(client: AsyncClient):
    """
    Test products update route
    :param client:
    :return:
    """
    response = await client.post("/products/update/1",
                                 json={
                                     "name": "Name1",
                                     "description": "Description1",
                                     "price": 10.2,
                                     "amount": 5,
                                     "is_service": 0
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_products_get_all(client: AsyncClient):
    """
    Test products get all routes
    :param client:
    :return:
    """
    response = await client.get("/products/")
    assert response.status_code == 200
    objs = json.loads(response.text)
    assert objs["success"] is True
    for obj in objs["data"]["products"]:
        assert obj["name"] == "Name1"
        assert obj["description"] == "Description1"
        assert obj["price"] == 10.2
        assert obj["amount"] == 5
        assert obj["is_service"] == 0
    assert objs["error"] is False


@pytest.mark.asyncio
async def test_product_delete(client: AsyncClient):
    """
    Test product delete route
    :param client:
    :return:
    """
    response = await client.post("/products/delete/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False
