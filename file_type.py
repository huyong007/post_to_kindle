'''
一个汽车的类
'''
class Car(object):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' +self.make+' '+self.model
        return long_name.title()
    def read_odomoter(self):
        print("This car has  "+str(self.odomoter_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odomoter_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")
    def increment_odometer(self,miles):
        self.odomoter_reading +=miles
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super(ElectricCar,self).__init__(make,model,year)
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a  "+str(self.battery_size)+"-kwh battery")

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

