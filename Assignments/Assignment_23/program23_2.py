class BankAccount:
    ROI = 10.5  # Rate of Interest

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account holder name:", self.Name)
        print("Account balance:", self.Amount)

    def Deposit(self, Value1):
        self.Amount = self.Amount + Value1
        return self.Amount

    def Withdraw(self, Value2):
        if Value2 > self.Amount:
            print("Insufficient balance!")
            return self.Amount
        self.Amount = self.Amount - Value2
        return self.Amount

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

def main():
    obj1 = BankAccount("Aaryaa", 5000)
    obj1.Display()
    print("Amount credited:", 1500)
    print("Balance:", obj1.Deposit(1500))
    print("Amount debited:", 1000)
    print("Balance:", obj1.Withdraw(1000))
    print("Rate of interest is:", obj1.CalculateInterest())

    print("")

    obj2 = BankAccount("Aishu", 3000)
    obj2.Display()
    print("Amount credited:", 1000)
    print("Balance:", obj2.Deposit(1000))
    print("Amount debited:", 1000)
    print("Balance:", obj2.Withdraw(1000))
    print("Rate of interest is:", obj2.CalculateInterest())

    print("")

    obj3 = BankAccount("Sangeeta", 11500)
    obj3.Display()
    print("Amount credited:", 1300)
    print("Balance:", obj3.Deposit(1300))
    print("Amount debited:", 3000)
    print("Balance:", obj3.Withdraw(3000))
    print("Rate of interest is:", obj3.CalculateInterest())


if __name__ == "__main__":
    main()
