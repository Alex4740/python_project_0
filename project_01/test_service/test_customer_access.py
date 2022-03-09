from project_01.customer_access.customer_access_imp import CustomerServiceImp
from project_01.customer_access.customer_entities import Customer
from project_01.customer_dao_layer.customer_dao_imp import CustomerDAOImp
from project_01.customer_dao_layer.customer_exceptions import BadCustomerInfo

customer_dao = CustomerDAOImp
customer_service = CustomerServiceImp(customer_dao)

def test_catch_first_name_to_long_create():
    customer = Customer(0, 1, "this is to long", 1000)
    try:
        customer_service.service_create_customer(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "first name is too long"

def test_catch_last_name_to_long_create():
    customer = Customer(0, 1, "this is fine", "this is too long last name", 1000)
    try:
        customer_service.service_create_customer(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Last name is too long"

def test_catch_first_name_too_long_update():
    customer = Customer(1,1, "too long first name")
    try:
        customer_service.service_update_customer_information(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "First name is too long"

def test_last_name_too_long_update():
    customer = Customer(0, 1, "this is fine", "this is too long last name", 1000)
    try:
        customer_service.service_update_customer_information(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "last name too long"

def test_non_int_provided_for_id_delete():
    try:
        customer_service.service_delete_customer_by_num("1")
    except BadCustomerInfo as e:
        assert str(e) == "please provide a valid number"

