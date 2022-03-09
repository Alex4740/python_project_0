""" this module is aboute customer class impelementation"""

from python_project.customer_dao_layer.customer_entities import Customer
from python_project.customer_dao_layer.customer_dao_interface import CustomerDAOInterface
from python_project.customer_dao_layer.customer_exceptions import NumNotFound

class CustomerDAOImp(CustomerDAOInterface):
    Customer_list = [Customer(1, "wr", "WR", 0)]
    num_generator = 2
    customer_list = []

    def __init__(self, customer_dao, customer):
        self.customer_list = []
        self.num_generator = int

    # create
    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_num = self.num_generator
        self.num_generator += 1
        self.customer_list.append(customer)
        return customer

    # read
    def get_customer_by_num(self, customer_num: int) -> Customer:
        for customer in self.customer_list:
            if customer.customer_num == customer_num:
                return customer
        raise NumNotFound("no customer with number input: please try again!")

    # update
    def update_customer_by_num(self, customer: Customer) -> Customer:
        for old_customer in self.customer_list:
            if old_customer.customer_num == customer.customer_num:
                old_customer = customer
            return old_customer
        raise NumNotFound("no customer match to the number given: please try again!")

    # delete
    def delete_customer_by_num(self, customer_num: int) -> bool:
        for customer in self.customer_list:
            if customer.customer_num == customer_num:
                self.customer_list.remove(customer)
            return True
        raise NumNotFound("No customer maches: please try again!")

    def withdrawal_method(self, value, account_num):
        pass



