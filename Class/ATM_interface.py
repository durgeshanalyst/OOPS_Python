class Atm:
    def __init__(self) -> None:
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input= input('''
                            Hello, How may I help you?
                          1. Enter 1 to create pin.
                          2. Enter 2 to deposit.
                          3. Enter 3 to withdraw.
                          4. Enter 4 to Check balance.
                          5. Enter 5 to Exit.''')
        if user_input==1:
            print('Create pin')
        elif user_input==2:
            print('Balance Check')
        elif user_input==3:
            print('Withdraw balance')
        elif user_input==4:
            print('Check balance')
        else:
            print('bye')

    def create_pin(self):
        self.pin= input('Enter your pin')
        print('Your pin set successfully !!')

    def deposit(self):
        temp=input('Enter your pin')
        if temp == self.pin:
            amaount = int(input('Enter Amount'))
            self.balance = self.balance + amaount
            print('Deposit successfull')
        else:
            print('Invalid pin')
    def withdraw(self):
        temp = input('Enter your Pin')
        if temp == self.pin:
            amount = int(input('Enter amount'))
            if amount < self.balance:
                self.balance = self.balance - amount
                print('Transaction done please collect balance')
            else:
                print('Insufficient balance')
        else:
            print('Invalid Pin')
    def check_balance(self):
        temp = input('Enter your PIn')
        if temp == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print('Invalid pin')