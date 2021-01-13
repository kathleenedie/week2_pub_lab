class Pub:
    
    def __init__(self, name, total_cash):
        self.name = name
        self.total_cash = total_cash

    def increase_in_till(self, price):
        self.total_cash += price
