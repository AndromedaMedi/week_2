from modules.Car import *
from modules.Engine import *
from modules.Gearbox import *

engine = Engine(2)
gearbox = GearBox(6)

car1 = Car("red", "Ford", engine, gearbox)
car2 = Car("white", "Audi", engine, gearbox)

print(car1.colour)
print(car1.engine.volume)
print(car1.engine.ignite())

