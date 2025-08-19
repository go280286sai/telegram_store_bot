"""
Test delivery db
"""
from app.services.delivery_data import DeliveryData


def test_delivery_db_create():
    """
    Test delivery db creation
    :return:
    """
    query = DeliveryData()
    result = query.create(name="Name", description="Description")
    assert result is True


def test_delivery_db_get_one():
    """
    Test delivery db get one
    :return:
    """
    query = DeliveryData()
    result = query.get_one(delivery_id=1)
    assert result['id'] == 1
    assert result['name'] == 'Name'
    assert result['description'] == 'Description'


def test_delivery_db_update():
    """
    Test delivery db update
    :return:
    """
    query = DeliveryData()
    result = query.update(
        delivery_id=1,
        name="Name2",
        description="Description2"
    )
    assert result is True


def test_deliveries_db_get_all():
    """
    Test deliveries db gets all
    :return:
    """
    query = DeliveryData()
    results = query.get_all()
    for result in results:
        assert result['id'] == 1
        assert result['name'] == 'Name2'
        assert result['description'] == 'Description2'


def test_delivery_db_delete():
    """
    Test delivery db delete
    :return:
    """
    query = DeliveryData()
    result = query.delete(delivery_id=1)
    assert result is True
