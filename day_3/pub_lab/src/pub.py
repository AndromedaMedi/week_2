
class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.stock = {}

    
    def drink_count(self):
        return len(self.drinks)
    
    def increase_till(self, drink_price):
        self.till += 3.50

    # def add_drink(self, drink):
    #     if drink in self.stock:
    #         self.stock[drink] += 1
    #     else:
    #         self.stock[drink] = 1

    # def stock_level(self, drink):
    #     if drink in self.stock:
    #         return self.stock[drink]
    #     else:
    #         return 0

    def stock_value(self):
        total = 0
        for drink in self.stock:
            total += (drink.price * self.stock[drink])


    def sell_drink_to_customer(self, customer, drink):
        if self.drinks.count(drink) == 0:
            return
        drink = self.drinks
        customer.reduce_money(self.drink.price)
        self.increase_till(self.drink.price )
   
    def can_serve(self, customer, drink):
        if not self.customer_is_old_enough(customer):
            return False
        if self.customer_too_drunk(customer):
            return False
        if not self.customer_can_afford_drink(customer, drink):
            return False
        if self.stock_level(drink) == 0:
            return False
        return True
    
    def serve(self, customer, drink):
        if self.can_serve(customer, drink):
            self.stock[drink] -= 1
            customer.buy_drink(drink)
            self.till += drink.price

