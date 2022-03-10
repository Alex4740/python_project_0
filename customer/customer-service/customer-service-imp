from abc import ABC

from python_project.customer_access.customer_access_interf import CustomerAccessInterface
from python_project.customer_dao_layer.customer_dao_interface import CustomerDAOInterface
from python_project.customer_dao_layer.customer_entities import Customer



class CustomerServiceImp(CustomerAccessInterface, ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        super().__init__(customer_dao)
        self.dao = None

    def service_create_customer(self, customer: Customer) -> Customer:
        if len(customer.first_name) > 20:
            raise BadCustomerInfo("First name is too long")
        elif len(customer.last_name) > 20:
            raise BadCustomerInfo("Last name is too long")
        for n in self.customer_dao.customer_list:



    def service_get_customer_info_by_num(self, customer_num: int) -> Customer:
        if type(customer_num) == int:
            return self.customer_dao.get_customer_by_num(customer_num)
        else:
            raise BadCustomerInfo("Please provide valid customer number")

    def

    def service_deposit_withdrawal(self, transaction_type: str, value, account_num) -> Customer:
        if transaction_type == "deposit":
            return self.dao.deposit_method(value, account_num)
        elif transaction_type == "withdrawal":
            return self.customer_dao.withdrawal_method(value, account_num)

    def service_deposit(self, value, account_num):
        return self.dao.deposite_method(value, account_num)

    def service_withdrawal(self, value, account_num):
        return self.dao.withdrawal_method(value, account_num)


    def service_delete_customer_by_num(self, customer_num: int) -> bool:
        if type(customer_num) == int:
            return self.customer_dao.delete_customer_by_num(customer_num)
        else:
            raise BadCustomerInfo("please provide valid customer number")




