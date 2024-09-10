# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
   # Prompt the user for savings account details
    print("Create a Savings Account:")
    savings_balance = float(input("Enter the initial savings balance: "))
    savings_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    savings_months = int(input("Enter the number of months: "))

    # Call the create_savings_account function
    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest_rate, savings_months
    )

    # Print the result for the savings account
    print(f"\nSavings Account Summary:")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Balance: ${updated_savings_balance:.2f}\n")
    
    # Prompt the user for CD account details
    print("Create a CD Account:")
    cd_balance = float(input("Enter the initial CD balance: "))
    cd_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    cd_months = int(input("Enter the number of months: "))

    # Call the create_cd_account function
    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest_rate, cd_months
    )

    # Print the result for the CD account
    print(f"\nCD Account Summary:")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Balance: ${updated_cd_balance:.2f}\n")

# Call the main function to run the program
if __name__ == "__main__":
    main()

