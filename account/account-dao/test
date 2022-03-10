"""This module contains account dao unit tests"""
from custom_exception import IdNotFound
from dal_layer.account_dao.account_dao_imp import AccountDAOImp
from entities_layer.account_class_information import Account

account_dao = AccountDAOImp()  # will use this object to all my account dao unit test.

"""
business logic:
           bank account may not have negative valuemat
           bank account must work with numbers
           banks must have unique account number
"""

def test_create_account_success():

    test_account = Account("RW Bank", 0, 0)
    result = account_dao.create_account(test_account)
    assert result.account_num != 0


def test_create_catch_non_unique_num():
    test_account = Account("F bank", 1, 0)
    result = account_dao.create_account(test_account)
    assert result.account_num != 1


"""
account balance test
"""


def test_create_account_balance_success():
    test_account = Account("RW Bank", 0, 0)
    result = account_dao.create_account(test_account)
    assert result.account_balance > 0


"""
account access
"""


def test_get_account_info_by_num_success():
    account_to_get = Account("test account", 0, 0)
    account_object_for_getting_num = account_dao.create_account(account_to_get)
    result = account_dao.get_account_info_by_num(account_object_for_getting_num.account_num)
    assert result.account_id == account_object_for_getting_num.account_num


def test_get_account_using_non_existant_num():
    try:
        account_dao.get_account_info_by_num(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account number match: please try again!"

"""
update by account id
"""

def test_update_account_by_num_success():
    account_name = Account("RW bank", 0, 0)
    result = account_dao.update_account_by_num(account_name)
    assert result.account_name == "RW bank"


def test_update_account_using_non_existant_num():
    try:
        new_account_name = Account("F bank", 1, 0)=
        account_dao.update_account_by_num(new_account_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account number match: please try again!"


"""
Delete account test
"""


def test_delete_account_by_num_success():
    result = account_dao.delete_account_by_num(1)
    assert result


def test_delete_account_with_non_existant_num():
    try:
        account_dao.delete_account_by_num(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account number match: please try again!"
