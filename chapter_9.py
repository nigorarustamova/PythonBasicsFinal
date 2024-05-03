class Car:
    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make

    def describe_car(self):
        print(f"The best car out there is {self.model} by {self.make}.")
        print(f"I bought my {self.make} in {self.year}")

    def fill_gas_tank(self):
        print(f"{self.model} uses 30 gallons of gasoline.")

car1 = Car('CX350', '2024', 'Lexus')
car2 = Car('Camry', '2018', 'Toyota')

car1.describe_car()
car2.describe_car()

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The battery size of the car is {self.battery_size} kwt battery")

class ElectricCar(Car):
    def __init__(self, model, year, make):
        super().__init__(model, year, make)
        self.battery = Battery()


    def fill_gas_tank(self):
        print(f'Electric car does not use gasoline.')

    def describe_electric(self):
        print(f"I bought {self.year} {self.model}.")
        print(f"My {self.model} is {self.color}.")

class ElectricCar(Battery):
    def __init__(self, model, year, make):
        super().__init__(model, year, make)
        self.battery_size = Battery()


electric_car1 = ElectricCar('Model Y', '2024', 'Tesla')
electric_car2 = ElectricCar('Highlander', '2022', 'Toyota')

print('____________________________')
electric_car1.describe_electric()
electric_car2.describe_electric()
electric_car1.describe_car()
electric_car2.describe_car()
electric_car1.describe_electric()
electric_car2.describe_electric()
electric_car2.fill_gas_tank()
electric_car2.describe_battery()


