""" this module is to test customer class implementation """
from project_01.customer_access.customer_entities import Customer
from project_01.customer_dao_layer.customer_dao_imp import CustomerDAOImp
from project_01.customer_dao_layer.customer_exceptions import NumNotFound

customer_dao = CustomerDAOImp()
"""
business rule
  customer may not have the same account number
  last name and first name may not exceed 20 characters

"""
"""
this test crafted to check two things
  1. for correct data input, the method return expected return
  2. when data doesn.t exist, does not exist message will displayed. 
"""


def test_create_customer_success():
    test_customer = Customer(0, "new", "customer", 10000)
    result = customer_dao.create_customer(test_customer)
    assert result.customer_num != 0

def test_catch_non_unique_num():
    """ my database handle customer number, i need to check the providing number"""

    test_customer = Customer(1,1,"Bad", "num", 1)
    result = customer_dao.create_customer(test_customer)
    assert result.customer_num != 1

"""
get customer test
"""
def test_get_customer_info_by_num_success():
    result = customer_dao.get_customer_by_id(1)
    assert result.customer_num == 1


def test_get_account_using_non_existant_num():
    try:
        customer_dao.get_customer_by_num(0)
        assert False
    except NumNotFound as e:
        assert str(e) == "No customer matches the number given: please try again!"

#update

def test_update_account_by_num_success():
    new_customer_name = Customer(1,1, "wr", "RW", 44)
    result = customer_dao.update_customer_by_num(new_customer_name)
    assert result.first_name == "wr"

def test_update_account_by_non_existant_num():
    try:
        new_customer_name = Customer(0,1, "wr", "WR", 44)
        customer_dao.update_customer_by_num(new_customer_name)
        assert False
    except NumNotFound as e:
        assert str(e) == "No customer matches the num given: please try again!"

# delete account
def test_delete_account_by_num_success():
    result = customer_dao.delete_customer_by_num(1)
    assert result

def test_delete_account_by_non_existant_num():
    try:
        customer_dao.delete_customer_by_num(0)
        assert False
    except NumNotFound as e:
        assert str(e) == "no customer matches:please try again!"




