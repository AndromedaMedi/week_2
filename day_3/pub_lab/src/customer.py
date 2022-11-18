
class Customer:
    
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness


    
    def reduce_money(self, drink_price):
        self.wallet -= drink_price 

    def suficient_funds(self, drink):
        return self.wallet >= drink.price

    def buy_drink(self, drink):
        if self.suficient_funds(drink):
            self.wallet -= drink.price
            self.drunkeness += drink.alcohol_level

    

