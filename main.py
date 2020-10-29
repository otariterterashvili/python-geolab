from car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class PetrolCar(Car):
    def __init__(self, make, model, year, tank_size):
        super().__init__(make, model, year)
        self.tank_size = tank_size
    def describe_tank(self):
        print("This car has a " + str(self.tank_size) + " Liter tank")

tesla = ElectricCar("Tesla", "Model s", 2019, 400)

tesla.read_full_name()
tesla.describe_battery()

bmw = PetrolCar("BMW", "F10", 2018, 80)
bmw.read_full_name()
bmw.describe_tank()

# car = Car("Toyota", "Rav4", 2018)




# car.read_full_name()
# car.increment_odometer(5)
# car.read_odometer()
# car.increment_odometer(100)
# car.read_odometer()
# car.update_odometer(1000)
# car.read_odometer()