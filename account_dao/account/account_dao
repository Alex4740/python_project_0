import account as Account

from account_dao_interface import AccountDAOInterface
from Python_project_0.custom_exception import IdNotFound


class AccountDAOImp(AccountDAOInterface):
    account_list = []
    num_generator = 2

    def __init__(self, name, balance):
        self.accounts_list = []
        self._name = name
        self.account_balance = account_balance
        self.accounts_list.append(account_needed_for_num_catch)
       

    def create_account(self, account: Account) -> Account:  # it gives account id and added to the list
        account.account_num = self.num_generator  # change the account id to newly generated one.
        self.num_generator += 1  # insure newly generated id.
        self.account_list.append(account)  # add new account to the database
        return account  # return new account with new id.

    def get_account_info_by_num(self, account_num: int) -> Account:
        for account in self.account_list:
            if account.account_num == account_num:
                return account
        raise NumNotFound("No account number match: please try again!")
        
    def get_all_account_info_by_num(self, account_list: int) -> Account:
        for account in self.account_list:
            if account.account_list == account_list:
                return account_list
        raise ListNotFound("no account number match: please try again!")
        
        
    def update_account_by_num(self, account: Account) -> Account:
        for old_account in self.account_list:
            if account.account_num == old_account.account_num:
                old_account = account
                return old_account
        raise IdNotFound("No account number match: please try again!")
        
    def update_account_deposit_withdrawal_by_num(self, account:Account) -> Account:
        transaction_type:int(value, account_num):
                if transaction_type == "deposite":
                    return self.dao.deposite_method(value, account_num)
                elif transaction_type == "withdrawal":
                    return self.dao.withdrawal_method(value,account_num)
                else:
                    return("thankyou for being value customer!")

    def delete_account_by_num(self, account_num: int)-> bool:
        for account in self.account_list:
            if account.account_num == account_num:
                self.account_list.remove(account)
                return True
        raise IdNotFound("No account number match: please try again!")

