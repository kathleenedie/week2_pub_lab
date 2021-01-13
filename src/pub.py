class Pub:
    
    def __init__(self, name, total_cash):
        self.name = name
        self.total_cash = total_cash

    def increase_in_till(self, price):
        self.total_cash += price

    def drink_purchase(self, customer, price):
        customer.customer_spends_money(price)
        self.increase_in_till(price)

    def check_customer_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False