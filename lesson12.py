# region lesson12
# def test_func(word):
#     print(word, end='')
#     print('!')
#
#
# test_func('Hi')
# test_func(5)
# test_func(5.6)
# def summa(a, b):
#     return a + b
#
#
# res = summa(5.5, 7.5)
# print(res)
# summa(5, 7)
# summa('H', 'i')
# def minimal(lis):
#     min1 = lis[0]
#     for el in lis:
#         if el < min1:
#             min1 = el
#     return min1
#
#
# nums1 = [5, 7, 9, 4]
# #
# print(minimal(nums1))
# # min1 = nums1[0]
# # for el in nums1:
# #     if el < min1:
# #         min1 = el
# #
# # print(min1)
# nums2 = [5.4, 7.3, 9.2, 4.1, 4.8]
# # min2 = nums2[0]
# # for el in nums2:
# #     if el < min2:
# #         min2 = el
#
# print(minimal(nums2))

# print((lambda x, y: x * y)(2, 5))
# endregion
# region task1
# def distance(time, speed):
#     return time * speed
#
#
# def km_end(a):
#     if a == 1:
#         return 'километр'
#     else:
#         return 'километров'
#
#
# result = distance(float(input('Скорость - ')), float(input('Время - ')))
# result_km = km_end(result)
# # result_km = (lambda a: 'километр' if a == 1 else 'километров')(result)
# print(f'Расстояние между объектами составляет {result} {result_km}')
# endregion
# region task2
# def func_print(word1, word2):
#     print(word1)
#     print(word2)
# func_print('Привет', 'мир')
# endregion
# region task3


# def newfunc(a):
#     def myfunc(b):
#         return a + b
#     return myfunc
#
#
# a = float(input('Введите число а - '))
# b = float(input('Введите число b - '))
# answer = newfunc(a)
# print(f'Сумма введенных чисел = {answer(b)}')


# def generate_power(exponent):
#     def power(func):
#         def inner_power(*args):
#             base = func(*args)
#             return base ** exponent
#         return inner_power
#     return power
#
#
# @generate_power(2)
# def raise_two(n):
#     return n
#
#
# @generate_power(3)
# def raise_three(n):
#     return n
#
#
# print(raise_two(5))
# print(raise_three(5))
# endregion
# region task4
# def divide(a, b, c=1):
#     if a != 0 and b != 0 and c != 0:
#         return a / b / c
#     else:
#         return 'Ошибка деления на 0'
#
#
# print(divide(1, 2))
# print(divide(10, 2, 0))
# endregion
# region task5
# def summ(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
#
# print(summ(1, 2, 3, 4, 5))
# endregion
# region task6
# def func(*args):
#     print(args)
#
#
# func(2, 4, 'Привет')
# (lambda *args: print(args))(2, 4, 'Привет')
# endregion




