from abc import ABC, abstractmethod

import account as Account


class AccountDAOInterface(ABC):


    # create
    @abstractmethod
    def create_account(self, account: Account)->Account:
        pass

    # read
    @abstractmethod
    def get_account_information_by_num(self, account_num: int)->Account:
        pass

    # update
    @abstractmethod
    def update_account_by_num(self, account: Account)->Account:
        pass

    # delete
    @abstractmethod
    def delete_account_by_num(self, account_num: int)->bool:
        pass


