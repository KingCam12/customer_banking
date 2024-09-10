"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_cd_account(balance, interest_rate, months):
 
    
    # Create an instance of the `Account` class and pass in the balance and interest as 0 for now
    cd_account = Account(balance, 0)
    
    # Calculate interest earned (assuming interest_rate is annual)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    
    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned
    
    # Set the updated balance using the set_balance method
    cd_account.set_balance(updated_balance)
    
    # Set the interest earned using the set_interest method
    cd_account.set_interest(interest_earned)
    
    # Return the updated balance and interest earned
    return updated_balance, interest_earned
