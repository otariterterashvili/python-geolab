class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.__owner = "Otar Terterashvili"

    def read_full_name(self):
        print(f"{self.make} {self.model} {self.year} year")
    
    def read_odometer(self):
        print(f"This car has {self.odometer} KM's on it")
        
    def update_odometer(self, km):
        if self.odometer > km:
            print("You can't roll back an odometer!")
        else:
            self.odometer = km

    def increment_odometer(self, km):
        self.odometer += km
