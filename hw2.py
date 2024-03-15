# Задача 1
# class Fruits:
#     def __init__(self, name,  color, weight ):
#         self.name = name 
#         self.color = color 
#         self.weight = weight
        
#     def info(self):
#         print(f"Name: {self.name}, Color:{self.color},  Weight: {self.weight}")
        
# Apple = Fruits("Яблоко", "Красный", 150)
# Banana = Fruits("Банан", "Желтый", 120)
# Orange = Fruits("Апелсин", "Оранжывый", 200)

# Apple.info()
# Banana.info()
# Orange.info()


# Задача2
# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
 
#     def drive(self, city):
#         print(f"Car - {self.model} is driving to {city}")
   
            
# Bmw = Car("m5 e60", 2007, "Black")
# Bmw.drive("New York")
# Доп Задача

# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.fuel = 0

#     def refuel(self, liters):
#         if liters > 40:
#             print("Вы не можете заправить более 40 литров за раз.")
#         else:
#             self.fuel += liters

#     def drive(self, city, distance):
#         fuel_need = distance / 10
#         if self.fuel >= fuel_need:
#             print(f"Машина - {self.model} едет в {city}, расстояние - {distance}")
#             self.fuel -= fuel_need
#         else:
#             remaining_distance = self.fuel * 10
#             print(f"Недостаточно топлива, чтобы добраться {city}. Автомобиль может идти {remaining_distance} км дальше.")
 
# bmw = Car('m5 e60', 2007, 'Black')
# bmw.drive('New York', 41)           
# bmw.refuel(40)    