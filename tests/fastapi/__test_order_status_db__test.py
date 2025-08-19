"""
Test order status db
"""
from app.services.order_status_data import OrderStatusData


def test_order_status_db_create():
    """
    Test user db creation
    :return:
    """
    query = OrderStatusData()
    result = query.create(status="Waite")
    assert result is True


def test_order_status_db_get_one():
    """
    Test order status db get one
    :return:
    """
    query = OrderStatusData()
    result = query.get_one(order_status_id=1)
    assert result['id'] == 1
    assert result['status'] == 'Waite'


def test_order_status_db_update():
    """
    Test order status db update
    :return:
    """
    query = OrderStatusData()
    result = query.update(order_status_id=1, status="Done")
    assert result is True


def test_order_status_db_get_all():
    """
    Test order status db get all
    :return:
    """
    query = OrderStatusData()
    results = query.get_all()
    for result in results:
        assert result['id'] == 1
        assert result['status'] == 'Done'


def test_order_status_db_delete():
    """
    Test order status db delete
    :return:
    """
    query = OrderStatusData()
    result = query.delete(order_status_id=1)
    assert result is True
