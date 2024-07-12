import argparse
from bank_account import BankAccount

def main():
    parser = argparse.ArgumentParser(description="Perform banking operations.")
    
    parser.add_argument('operation', choices=['deposit', 'withdraw', 'balance'], 
                        help="The operation to perform.")
    parser.add_argument('amount', type=float, nargs='?', default=0, 
                        help="The amount to deposit or withdraw.")
    
    args = parser.parse_args()

    # Creating a BankAccount instance
    account = BankAccount()

    if args.operation == 'deposit':
        account.deposit(args.amount)
        print(f"Deposited ${args.amount:.2f}")
        account.display_balance()

    elif args.operation == 'withdraw':
        success = account.withdraw(args.amount)
        if success:
            print(f"Withdrew ${args.amount:.2f}")
        else:
            print(f"Insufficient funds to withdraw ${args.amount:.2f}")
        account.display_balance()

    elif args.operation == 'balance':
        account.display_balance()

if __name__ == '__main__':
    main()
