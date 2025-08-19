"""
User route test
"""
# pylint: disable=redefined-outer-name
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
async def test_users_get_one(client: AsyncClient):
    """
    Test user get one route
    :param client:
    :return:
    """
    response = await client.get("/users/get/1")
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"]["name"] == "User"
    assert obj["data"]["username"] == "Username"
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_user_update(client: AsyncClient):
    """
    Test user update route
    :param client:
    :return:
    """
    response = await client.post("/users/update/1",
                                 json={
                                     "name": "User1",
                                     "username": "Username1"
                                 })
    assert response.status_code == 200
    obj = json.loads(response.text)
    assert obj["success"] is True
    assert obj["data"] is None
    assert obj["error"] is False


@pytest.mark.asyncio
async def test_users_get_all(client: AsyncClient):
    """
    Test users get all routes
    :param client:
    :return:
    """
    response = await client.get("/users/")
    assert response.status_code == 200
    objs = json.loads(response.text)
    assert objs["success"] is True
    for obj in objs["data"]["users"]:
        assert obj["name"] == "User1"
        assert obj["username"] == "Username1"
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
