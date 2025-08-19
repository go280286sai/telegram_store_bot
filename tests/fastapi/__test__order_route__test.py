"""
Order route test
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
async def test_user_create(client: AsyncClient):
    """
    Test user creates route
    :param client:
    :return:
    """
    response = await client.post("/users/create",
                                 json={
                                     "name": "User",
                                     "username": "Username"
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


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
async def test_order_create(client: AsyncClient):
    """
    Test order creates route
    :param client:
    :return:
    """
    response = await client.post("/orders/create",
                                 json={
                                     "status_id": 1,
                                     "product_id": 1,
                                     "delivery_id": 1,
                                     "user_id": 1
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_order_get_one(client: AsyncClient):
    """
    Test delivery get one route
    :param client:
    :return:
    """
    response = await client.get("/orders/get/1")
    assert response.status_code == 200
    objs = json.loads(response.text)
    assert objs["success"] is True
    for obj in objs['data']:
        assert obj["delivery_id"] == 1
        assert obj["order_status_id"] == 1
        assert obj["product_id"] == 1
        assert obj["user_id"] == 1
        assert obj["delivery_name"] == "Name"
        assert obj["order_status_name"] == "Wait"
        assert obj["product_name"] == "Name"
        assert obj["username"] == "Username"
    assert objs["error"] is False


@pytest.mark.asyncio
async def test_order_update(client: AsyncClient):
    """
    Test order update route
    :param client:
    :return:
    """
    response = await client.post("/orders/update/1",
                                 json={
                                     "status_id": 1,
                                     "product_id": 1,
                                     "delivery_id": 1,
                                     "user_id": 1
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_orders_get_all(client: AsyncClient):
    """
    Test orders get all routes
    :param client:
    :return:
    """
    response = await client.get("/orders/")
    assert response.status_code == 200
    objs = json.loads(response.text)
    assert objs["success"] is True
    for obj in objs['data']['orders']:
        assert obj["delivery_id"] == 1
        assert obj["order_status_id"] == 1
        assert obj["product_id"] == 1
        assert obj["user_id"] == 1
        assert obj["delivery_name"] == "Name"
        assert obj["order_status_name"] == "Wait"
        assert obj["product_name"] == "Name"
        assert obj["username"] == "Username"
    assert objs["error"] is False


@pytest.mark.asyncio
async def test_user_delete(client: AsyncClient):
    """
    Test user delete route
    :param client:
    :return:
    """
    response = await client.post("/users/delete/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


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


@pytest.mark.asyncio
async def test_order_delete(client: AsyncClient):
    """
    Test orders delete route
    :param client:
    :return:
    """
    response = await client.post("/orders/delete/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False
