class Customer:
    def __init__ (self, customer, wallet, age):
        self.customer = customer
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0
      

    def customer_spends_money(self, price):
        self.wallet -= price