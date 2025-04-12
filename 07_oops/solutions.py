class Car : 
    def __init__(self , userbrand , usermodel):
        self.brand = userbrand 
        self.model = usermodel
    def full_name(self):
        return f"{self.brand} {self.model}"
    def get_brand(self):
        return self.brand + " sad"
class ElectricCar(Car):
    def __init__(self,brand , model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

tesla_car = ElectricCar("toyota" , "corolla " , "2300mh")


print(tesla_car.get_brand())
print(tesla_car.brand)
# print(tesla_car.model)
# print(tesla_car.battery_size)

# my_car = Car("toyota " , "corolla")
# print(my_car.brand)
# print(my_car.full_name())


# my_other_car = Car("tata" , "safari")
# print(my_other_car.brand)
