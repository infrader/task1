class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Autobus(Transport):
    pass 

bus = Autobus("Renault Logan", 180, 12)

print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")