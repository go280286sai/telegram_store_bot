"""
Test product db
"""
from app.services.product_data import ProductData


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


def test_product_db_get_one():
    """
    Test product db get one
    :return:
    """
    query = ProductData()
    result = query.get_one(product_id=1)
    assert result['id'] == 1
    assert result['name'] == 'Name'
    assert result['description'] == 'Description'
    assert result['price'] == 10.78
    assert result['is_service'] == 0
    assert result['amount'] == 10


def test_product_db_update():
    """
    Test product db update
    :return:
    """
    query = ProductData()
    result = query.update(
        product_id=1,
        name="Name2",
        description="Description2",
        is_service=0,
        price=12.78,
        amount=8
    )
    assert result is True


def test_products_db_get_all():
    """
    Test products db gets all
    :return:
    """
    query = ProductData()
    results = query.get_all()
    for result in results:
        assert result['id'] == 1
        assert result['name'] == 'Name2'
        assert result['description'] == 'Description2'
        assert result['price'] == 12.78
        assert result['is_service'] == 0
        assert result['amount'] == 8


def test_product_db_delete():
    """
    Test product db delete
    :return:
    """
    query = ProductData()
    result = query.delete(product_id=1)
    assert result is True
