""" interface for account service object to check and validate the data for business rule and programing logic
"""
from abc import ABC, abstractmethod

from account.models import Account


class AccountServiceInterface(ABC):


#create abstract account

    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
""" this method validate the account information to pass correct data to DAL"""
        pass

# read
    @abstractmethod
    def service_get_account_information_by_num(self, account_num: str) -> Account:
""" validate correct identifier is being used before passing to DAL"""
        pass

# update
    @abstractmethod
    def service_update_account_by_num(self, account: Account) -> Account:
""" to validate account information befor passing to DAL for upgrade"""
        pass
#delete
    @abstractmethod
    def service_delete_account_by_num(self, account_num: int) ->bool:
""" validate the correct identifier is being used before passing to DAL"""
        pass




