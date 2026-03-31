class Account:
    def __init__(self, acc_no, amt=0.0):
        self.acc_no = acc_no
        self.amt = amt

    def add_money(self, value):
        if value > 0:
            self.amt += value
            print(f"Deposited: ${value:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def take_money(self, value):
        if value > 0 and value <= self.amt:
            self.amt -= value
            print(f"Withdrawn: ${value:.2f}")
        elif value > self.amt:
            print("Insufficient balance!")
        else:
            print("Withdrawal amount must be greater than zero.")

    def show_balance(self):
        print(f"Account {self.acc_no} Balance: ${self.amt:.2f}")


acc = Account(123456789, 5000.00)

acc.show_balance()
acc.add_money(2000)
acc.take_money(1000)
acc.show_balance()