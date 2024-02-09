# region lesson14
# y = False
# while y == False:
#     try:
#         x = int(input('Введите число: '))
#         x += 5
#         print(x)
#         y = True
#     except ValueError:
#         print('Введите лучше число!')
# try:
#     x = 5 / 1
# except ZeroDivisionError:
#     print('Ошибка деления на 0')
# except ValueError:
#     print('Вы ввели что то не так')
# else:
#     print('else')
# finally:
#     print('Finally')
# endregion
# region task1
# while True:
#     try:
#         age = int(input('Введите свой возраст: '))
#         break
#     except ValueError:
#         print("Введите число!")
# print(age)
# endregion
# region task2
# try:
#     y +=1
# except NameError:
#     print('Ошибка имени переменной')
# endregion
# region task3
# def summa(*nums):
#     result = 0
#     for num in nums:
#         result += num
#     return result
#
#
# try:
#     print(summa(1234, 456, 283))
#
# except NameError:
#     print("Ошибка имени функции")
# endregion
# region task 4
# try:
#     file = open('lesson14/text.txt', 'r')
#     file.close()
# except FileNotFoundError:
#     print('Такого файла не существует')
# endregion
# region task5
# file = open("lesson14/example.txt", 'w')
# file.close()
# try:
#     file = open('lesson14/example.txt', 'x')
# except FileExistsError:
#     file = open('lesson14/example.txt', 'a')
# finally:
#     file.close()
# endregion





