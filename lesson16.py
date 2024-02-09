# region dir_lesson16
# import time
# time.sleep(3)
# print('Hello')
# import datetime as d
# print(d.datetime.now().time())
# import sys, os, platform
# print(sys.path)
# print(platform.system())
# from math import sqrt, ceil
# print(ceil(sqrt(100)))
# with open('dir_lesson16/mymodule.py', 'w') as file:
#     file.write('Hello')
# from pprint import pprint
# import dir_lesson16.mymodule as mymodule
# import importlib
# import sys
# pprint(sys.path)
# pprint(mymodule.name)
# mymodule.name = 'Sasha'
# pprint(mymodule.name)
# importlib.reload(mymodule)
# pprint(mymodule.name)
# print(mymodule.name)
# print(mymodule.add_three_numbers(4, 3, 8))
# endregion
# region task1
# from math import ceil as c, pi
# print(pi)
# print(c(10.8))
# endregion
# region task2
# import dir_lesson16.module_task2 as module_task2
# print(module_task2.summa(2, 4))
# endregion
# region task3
# from random import randint
# num = randint(0, 20)
# count = 0
# while True:
#     count += 1
#     while True:
#         try:
#             input_num = int(input("Введите целое число от 0 до 20: "))
#             if input_num < 0 or input_num > 20:
#                 print("Число не соответствует диапазону")
#             else:
#                 break
#         except ValueError:
#             print("Некорректный ввод числа")
#     if input_num == num:
#         print("Поздравляем! Вы угадали!")
#         break
#     elif input_num > num:
#         print("Вы не угадали!")
#         print("Число что вы пытаетесь угадать меньше")
#     else:
#         print("Вы не угадали!")
#         print("Число что вы пытаетесь угадать больше")
# print(f'Количество попыток: {count}')
# endregion
# region task4
# from datetime import datetime as date
# print(date.now().date())
# endregion
