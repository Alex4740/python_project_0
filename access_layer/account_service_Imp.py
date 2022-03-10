""" the module to implement the account service interface. it validates and define how the data works and what needs to happen
if not validated"""

from account.models import Account, account

from Python_project_0.access_layer.account_service_interface import AccountServiceInterface
from Python_project_0.custom_exception import BadAccountName
from Python_project_0.dal_layer.account_dao.account_dao_interface import AccountDAOInterface


class AccountServiceImp(AccountServiceInterface):

    def __init__(self, account_dao: AccountDAOInterface, account_valance):
        self.account_dao = account_dao
        self.account_balance = account_balance

        existing_account = account
<<<<<<< HEAD
        

    def service_create_account(self, account: Account) -> Account:
        if type(account.account_name) != str:              # to check the account name is string or not
            raise BadAccountName("please pass valid name")                 # raise exception for non str.from
        elif type(account.account_balance: int) < 0:                       # check the account balace negative 
            raise BadAccountBalance("please pass non negetive balance")    # raise exception for negative account balance
        for existing_account_in_self.account_dao.account_list:             # makes loop through existing accounts to validate business rules
            if existing_account.account_name == account.account_name:      # here chack for duplicate account name
                raise BadAccountName("this name already exist")            # raise exception for duplicate Account name
        return self.account_dao.create_account(account)                    # all validation checked and pass the data to DAL


    
    def service_get_account_info_by_num(self, account_num: str) -> Account:
        try:
            return self.account_dao.get_account_info_by_num(int(account_num))
        except valueError:
            raise BadAccountInfo("please provide a valid account num")

        

    def service_update_by_account_num(self, account: Account) -> Account:
        if type(account.account_name) != str:        # this check account name is string or not
            raise BadAccountInfo("please provide valid account name")        # raise exception for not using string
        elif existing_account.account_name == account.account_name:          # checking for duplicate account name.
            raise BadAccountInfo("account already exist")                    # raise exception to duplicate name
        return self.account_dao.update_account_by_account_num(account)   # assume all validation checked, pass to DAL
    

    def service_delete_account_by_num(self, account_num: int) -> bool:
        if type(account_num) == int:
            return self.account_dao.delete_account_by_num(account_num)
        else:
            raise BadAccountInfo("please provide valid account number)
        

    def service_create_account(self, account: Account) -> Account:
        if type(account.account_name) != str:                        # to check the account name is string
            raise BadAccountName("please pass valid name")           # raise exception for not working with a string
        elif type(account.account_balance) < 0 int:                  # check for non posetive account balance
            raise BadAccountInfo("please pass non negetive account balance")   # raise exception for non posetive account balance
        for existing_account_in_self.account_dao.account_list:       # here need to loop through existing account for validation
            if existing_account.account_name == account.account_name:    # checking for duplicate account name
                raise BadAccountName("this name already exist")          # raise exception for duplicate account name
        return self.account_dao.create_account(account)               # assume all validation checked, pass to DAL
    
    
    def service_get_account_information_by_num(self, account_num: str) -> Account:
        try:
            return self.account_dao.get_account_info_by_num(int(account_num))
        except valueError:
            raise BadAccountInfo("please provide a valid account_num")
            
     def service_update_by_account_num(self, account: Account) -> Account:
        if type(account.account_name) != str:       #checking for using string
            raise BadAccountInfo("please pass in valid account name")    # raise exception for not using string
        for existing_account in self.account_dao.account_list:   # looping through existing account to validate buisness rule.
            if existing_account.account_name == account.account_name:   # checking for duplicate name
                raise BadAccountInfo("name already exist")        # raise exception for duplicate account name
         return self.account_dao.update_by_account_num(account)    # assume all validation checked, pass in to DAL
    
    def service_delete_account_by_num(self, account_num: int) -> bool:
        it type(account_num) == int:
            return self.account_dao.delete_account_by_num(account_num)
        else:
            raise BadAccountInfo("please provide a valid account-num)
                                 

>>>>>>> 795c292679628c55f12c804a8440eb8839d03df5
