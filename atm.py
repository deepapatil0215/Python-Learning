def balance_check(balance):
    print("this is a balance amount:"+str(balance))
def withdraw(pin,amount,balance):
    print("entered amount is"+str(amount))
    current_balance = balance - amount
    print("your current balance is:"+str(current_balance))
def main():
    balance = 1000
    print("1.Withdraw")
    print("2.Balance Check")
    print("3.Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        pin = int(input("enter the pin number"))
        amount = int(input("enter the amount"))
        withdraw(pin,amount,balance)
    elif choice == 2:
        balance_check(balance)
    elif choice == 3 :
        print("Exit")
main()


