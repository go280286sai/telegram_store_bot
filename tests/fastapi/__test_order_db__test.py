"""
Test order db
"""
from app.services.delivery_data import DeliveryData
from app.services.order_data import OrderData
from app.services.order_status_data import OrderStatusData
from app.services.product_data import ProductData
from app.services.users_data import UsersData


def test_delivery_db_create():
    """
    Test delivery db creation
    :return:
    """
    query = DeliveryData()
    result = query.create(name="Name", description="Description")
    assert result is True


def test_order_status_db_create():
    """
    Test user db creation
    :return:
    """
    query = OrderStatusData()
    result = query.create(status="Wait")
    assert result is True


def test_product_db_create():
    """
    Test product db creation
    :return:
    """
    query = ProductData()
    result = query.create(
        name="Name",
        description="Description",
        price=10.78,
        is_service=0,
        amount=10
    )
    assert result is True


def test_user_db_create():
    """
    Test user db creation
    :return:
    """
    user = UsersData()
    result = user.create(name="User", username="UserName")
    assert result is True


def test_order_db_create():
    """
    Test order db creation
    :return:
    """
    query = OrderData()
    result = query.create(
        user_id=1,
        delivery_id=1,
        status_id=1,
        product_id=1
    )
    assert result is True


def test_order_db_get_one():
    """
    Test order db get one
    :return:
    """
    query = OrderData()
    results = query.get_one(order_id=1)
    assert results is not None
    for result in results:
        assert result['id'] == 1
        assert result['delivery_id'] == 1
        assert result['order_status_id'] == 1
        assert result['product_id'] == 1
        assert result['user_id'] == 1
        assert result['delivery_name'] == 'Name'
        assert result['order_status_name'] == 'Wait'
        assert result['product_name'] == 'Name'
        assert result['username'] == 'UserName'


def test_order_db_update():
    """
    Test order db update
    :return:
    """
    query = OrderData()
    result = query.update(
        order_id=1,
        product_id=1,
        user_id=1,
        delivery_id=1,
        status_id=1
    )
    assert result is True


def test_orders_db_get_all():
    """
    Test orders db gets all
    :return:
    """
    query = OrderData()
    results = query.get_all()
    assert results is not None
    for result in results:
        assert result['id'] == 1
        assert result['delivery_id'] == 1
        assert result['order_status_id'] == 1
        assert result['product_id'] == 1
        assert result['user_id'] == 1
        assert result['delivery_name'] == 'Name'
        assert result['order_status_name'] == 'Wait'
        assert result['product_name'] == 'Name'
        assert result['username'] == 'UserName'


def test_order_db_get_all_user():
    """
    Test order db gets all users
    :return:
    """
    query = OrderData()
    results = query.get_all_user(user_id=1)
    assert results is not None
    for result in results:
        assert result['id'] == 1
        assert result['delivery_id'] == 1
        assert result['order_status_id'] == 1
        assert result['product_id'] == 1
        assert result['user_id'] == 1
        assert result['delivery_name'] == 'Name'
        assert result['order_status_name'] == 'Wait'
        assert result['product_name'] == 'Name'
        assert result['username'] == 'UserName'


def test_order_db_delete():
    """
    Test order db delete
    :return:
    """
    query = OrderData()
    result = query.delete(order_id=1)
    assert result is True


def test_user_db_delete():
    """
    Test user db delete
    :return:
    """
    user = UsersData()
    result = user.delete(user_id=1)
    assert result is True


def test_product_db_delete():
    """
    Test product db delete
    :return:
    """
    query = ProductData()
    result = query.delete(product_id=1)
    assert result is True


def test_order_status_db_delete():
    """
    Test order status db delete
    :return:
    """
    query = OrderStatusData()
    result = query.delete(order_status_id=1)
    assert result is True


def test_delivery_db_delete():
    """
    Test delivery db delete
    :return:
    """
    query = DeliveryData()
    result = query.delete(delivery_id=1)
    assert result is True
