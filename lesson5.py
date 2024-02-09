# region lesson5
# user_data = int(input("Введите число: "))
#
# is_happy = False
#
# if is_happy:
#     print('User is Happy')
# else:
#     print('User is unhappy')
#

# if user_data == 5:
#     print('Number is 5')
# elif user_data > 5:
#     print('Number is bigger than 5')
# else:
#     print('Number is smaller than 5')

# data = input()
# number = 5 if data == 'Five' else 0
# if data == 'Five':
#     number = 5
# else:
#     number = 0

# print(number)
# endregion
# region task1
# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
# if a%2 == 0:
#     print('Число а четное')
# else:
#     print('Число а нечетное')
# if b%2 == 0:
#     print('Число b четное')
# else:
#     print('Число b нечетное')
# endregion
# region task2-task3
# def input_num(text_input=''):
#     number = input(text_input)
#     try:
#         number = int(number)
#     except ValueError:
#         try:
#             number = float(number)
#         except ValueError:
#             print('Неверный формат числа')
#             number = input_num(text_input)
#     return number
#
#
# def input_operation():
#     operation = input('Введите оператор: ')
#     match operation:
#         case '+':
#             return operation
#         case '-':
#             return operation
#         case '*':
#             return operation
#         case '/':
#             return operation
#         case _:
#             print('Неверный оператор')
#             operation = input_operation()
#             return operation
#
#
#
# num1 = input_num('Введите первое число: ')
# operation = input_operation()
# num2 = input_num('Введите второе число: ')
#
# match operation:
#     case '+':
#         result = num1 + num2
#     case '-':
#         result = num1 - num2
#     case '*':
#         result = num1 * num2
#     case '/':
#         result = (num1 / num2) if num2 != 0 else 'Ошибка при делении на 0'
#
# print(f'{num1} {operation} {num2} = {result}')

# endregion
# region task4
# a = 14
# if (a > 10 and a!= 12 and a <= 15) or a == 18:
#     print('True')
# endregion
