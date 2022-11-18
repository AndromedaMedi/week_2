from classes.vehicle import Vehicle

class Motorbike(Vehicle):
    def start_engine(self):
        super_start_val = super().start_engine()
        print(super_start_val)
        return "Meow"
