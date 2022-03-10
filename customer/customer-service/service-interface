from abc import ABC, abstractmethod

from python_project.customer_dao_layer.customer_dao_imp import CustomerDAOImp
from python_project.customer_dao_layer.customer_dao_interface import CustomerDAOInterface
from python_project.customer_dao_layer.customer_entities import Customer


class CustomerAccessInterface(ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao: CustomerDAOImp = customer_dao


    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_info_by_num(self, customer_num: int) -> Customer:
        pass

    @abstractmethod
    def service_update_customer_info(self, customer:Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_num(self, customer: Customer) -> bool:
        pass







