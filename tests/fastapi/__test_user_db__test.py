"""
Test user db
"""
from app.services.users_data import UsersData


def test_user_db_create():
    """
    Test user db creation
    :return:
    """
    user = UsersData()
    result = user.create(name="User", username="UserName")
    assert result is True


def test_user_db_get_one():
    """
    Test user db get one
    :return:
    """
    user = UsersData()
    result = user.get_one(user_id=1)
    assert result['id'] == 1
    assert result['username'] == 'UserName'
    assert result['name'] == 'User'


def test_user_db_update():
    """
    Test user db update
    :return:
    """
    user = UsersData()
    result = user.update(user_id=1, name="User2", username="UserName2")
    assert result is True


def test_user_db_get_all():
    """
    Test user db get all
    :return:
    """
    user = UsersData()
    results = user.get_all()
    for result in results:
        assert result['id'] == 1
        assert result['username'] == 'UserName2'
        assert result['name'] == 'User2'


def test_user_db_delete():
    """
    Test user db delete
    :return:
    """
    user = UsersData()
    result = user.delete(user_id=1)
    assert result is True
