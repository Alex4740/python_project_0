"""this module is about customer abstract class"""
from abc import ABC, abstractmethod

from python_project.customer_dao_layer.customer_entities import Customer


class CustomerDAOInterface(ABC):
   # create
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass


# read
    @abstractmethod
    def get_customer_by_id(self, customer_num: int):
        pass
#update
    @abstractmethod
    def update_customer_by_id(self, customer_num: int):
        pass

#delete
    @abstractmethod
    def delete_customer_by_id(self, customer_num: int) -> Customer:
        pass


