class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed
    
    def get_car_name(self):
        return f"{self.make} {self.model}"

my_car = Car("Corrola", "Toyota", 2025)
print(f"Назва машини: {my_car.get_car_name()}")

for _ in range(5):
    my_car.accelerate()
    print(f"Поточна швидкість: {my_car.get_speed()}")

for _ in range(5):
    my_car.brake()
    print(f"Поточна швидкість: {my_car.get_speed()}")
