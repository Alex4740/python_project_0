""" this test is to insure my methods when implemented will perform necessery validation on the data"""


from account.models import Account
from Python_project_0.access_layer.account_service_Imp import AccountServiceImp
from Python_project_0.custom_exception import BadAccountName
from Python_project_0.dal_layer import account_dao

duplicate_account_name = Account("name", 0, 0)
account_service = AccountServiceImp(account_dao)
account_dao = AccountDAO()
non_string_account_name = Account(account name, 0, 0)
duplicate_account_num = Account(account name, account number, 0)
duplicate_account_name = Account(account name, 0, 0)
non_negative_account_balance = Account(account name, 0, 0)
""" 
buseness rule
     account may not have the same name
     account may not have negetive balance
     account my not have duplicate account number
"""
   
def test_check_no_duplicate_account_name():
    try:
        account_service.service_create_account(duplicate_account_name)
        assert False
    except BadAccountName as e:
        assert str(e) == "this name is already exist"

def test_check_non_string_create_account():
    try:
        account_service.service_create_account(non_string_account_name)
        assert False
    except BadAccountName as e:
        assert str(e) == "please pass valid account name"
     
def test_check_no_negetive_account_balance():
    try:
        account_service.service_create_account(no_negative_account_balance)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "please pass non negetive account balance"

        
def test_cant_type_to_int():
    try:
        account_service.service_get_account_info_by_num("one")
        assert False
    except BadAccountInfo as e:
        assert str(e) == "please provide a valid account num"
        
        
def test_get_account_success_typecast_string():
    result = account_service.service_get_account_info_by_num("1")
    assert result.account_num == 1
    
    
def test_check_no_duplicate_names_update_account():
        try:
            account_service.service_update_account_by_num(duplicate_account_name_update)
            assert False
         except BadAccountInf as e:
            assert str(e) == " the account name already exist"
            
def test_catch_non_string_account_name_update_account():
    try:
        account_service.service_update_account_by_num(non_tring_account_name_update)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "please pass in valid account name"
        
def test_catch_non_numeric_num_delete_account():
    try:
        account_service.service_delete_account_by_num("one")
        assert False
     except BadAccountInfo as e:
        assert str(e) == "please provide valid account num"
        
          
