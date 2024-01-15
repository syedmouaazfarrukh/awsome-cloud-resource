
# Add all the necessary libraries in `requirements.txt`

class AccountManager:
    def account_exist(self, customer_id):
        # Check in the table wether the customer exists or not
        pass

    def create_account(self, customer_id, initial_balance):
        # create a new account for the customer with the specified initial balance
        pass

    def get_account_balance(self, customer_id, account_id):
        # Logic to retrieve the account balance for the given account ID
        pass

    def get_account_details(self,customer_id, account_id):
        # Logic to retrieve the account balance for the given account ID
        pass


if __name__ == "__main__":
    
    # Create a database and in it a tables with customer id, account id and balance details
    
    account_manager = AccountManager()
    account_manager.create_account(customer_id="12345", initial_balance=1000)
    balance = account_manager.get_account_balance(account_id="67890")
    print(f"Account Balance: ${balance}")


