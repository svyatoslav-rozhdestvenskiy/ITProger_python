# region lesson19
# class Building:
#     __year = None
#     city = None
#
#     def __init__(self, year=None, city=None):
#         self.year = year
#         self.city = city
#         self.get_info()
#
#     def get_info(self):
#         print("\nГод постройки здания:", self.year)
#         print(f'Город постройки здания: {self.city}')
#
#
# class School(Building):
#     pupils = 0
#
#     def __init__(self, year=None, city=None, pupils=0):
#         super(School, self).__init__(year, city)
#         self.pupils = pupils
#
#     def get_info(self):
#         super(School, self).get_info()
#         print(f'Тип здания: Школа')
#         print(f'Количество учеников: {self.pupils}')
#
#
# school = School(2000, 'Moscow', 1022)
# school.year = 5
# print(school.year)
# endregion
# region task1
# class Car:  # Создание класса
#     wheels = 4  # Несколько полей
#     model = "Some"
#     speed = 123.5
#
#     def set(self, wheels, model, speed, **kwargs):  # Метод для установки значений
#         self.wheels = wheels
#         self.model = model
#         self.speed = speed
#
#     def getAll(self):  # Метод для вывода значений
#         print("Автомобиль ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels,
#               " колесах!")
#         pass
#
#
# class Motorbike(Car):
#     engine = None
#
#     def set(self, wheels, model, speed, **kwargs):
#         super(Motorbike, self).set(wheels, model, speed)
#         self.engine = kwargs.get('engine')
#
#     def getAll(self):  # Метод для вывода значений
#         super().getAll()
#         print('А также имеет двигатель работающий на:', self.engine)
#
#
#
#
# motorbike = Motorbike()
# motorbike.set(4, 'traktor', 120, engine='diesel fuel')
# motorbike.getAll()
# car = Car()
# car.set(4, 'subaru', 180)
# car.getAll()
# endregion
# region task2_3_4
# class Car:
#     wheels = 4
#     model = "Some"
#     speed = 123.5
#
#     def __init__(self, wheels, model, speed):
#         self.wheels = wheels
#         self.model = model
#         self.speed = speed
#
#     def set(self, wheels, model, speed):
#         self.wheels = wheels
#         self.model = model
#         self.speed = speed
#
#     def getAll(self):
#         self.__protected()
#
#     def __protected(self):
#         print("Транспорт ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")
#
#
# class Motorcycle(Car):
#     engine = "Default"
#
#     def __init__(self, wheels, model, speed, engine):
#         super(Motorcycle, self).__init__(wheels, model, speed)
#         self.engine = engine
#
#     def getAll(self):
#         super().getAll()
#         print("Его двигатель:", self.engine)
#
# shkoda = Car(4, "Shkoda", 125.45)
# shkoda.getAll()
#
# audi = Car(4, "Audi", 250.9)
# audi.getAll()
#
# print("")  # Просто пропуск строки
#
# harley = Motorcycle(2, "Harley Davidson", 200, "Powerfull")
# harley.getAll()
# endregion

