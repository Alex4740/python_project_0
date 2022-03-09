""" this module is about customer class objects, I will go with customer ID, last name first name and account number"""


class Customer:

    def __init__(self, customer_num: int, last_name: str, first_name: str, account_num: int):
        self.customer_num = customer_num
        self.last_name = last_name
        self.first_name = first_name
        self.account_num = account_num


"""
what customers have in real life

customers have name
customers have account
customers have family
customers have id

"""
