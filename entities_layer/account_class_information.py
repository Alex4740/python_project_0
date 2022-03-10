class Account:
    def __init__(self, account_name:str, account_num:int, account_balance:int):
        self.account_name = account_name
        self.account_num = account_num
        self.account_balance = account_balance
    
    
    def convert_to_dictionary(self):
        return {
            "accountNum": self.account_num,
            "accountName": self.account_name,
            "accountBalance": self.account_balance
        }

# what account is made of
"""
Account have users
account have names
have account numbers
account have balance

from the above, my entitis will go with names, account numbers and balance. Users are customers which have there own class
"""
