# region lesson10
# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# country = dict(code='RU', name='Russian')
# print(country)
# print(country.items())
# for key, value in country.items():
#     print(key, '-', value)
# print(country.get('name'))
# # country.clear()
# country.popitem()
# lis = list(country.items())
# print(lis[0])
# country.update(code='ua', winter='cold')
# print(country)
# person = {
#     'user_1': {
#         'first_name': 'John',
#         'last_name': 'Marley',
#         'age': 45,
#         'address': {
#             'city': 'Moscow',
#             'street': 'red square',
#             'house': 24
#         },
#         'grades': {'math': 5, 'physics': 4}
#     },
#     'user_2': {
#         'first_name': 'John',
#         'last_name': 'lemon',
#         'age': 32,
#         'address': {
#             'city': 'Moscow',
#             'street': 'red square',
#             'house': 43
#         },
#         'grades': {'math': 4, 'physics': 4}
#
#     }
# }
# print(person['user_1']['grades']['math'])
# endregion
# region task1

# код курильщика
# i = 0
# student = {}
# while True:
#     student_count = input('Введите количество студентов: ')
#     try:
#         student_count = int(student_count)
#         break
#     except ValueError:
#         print('Неверный формат числа')
# while i < student_count:
#     input_text_name = 'Введите имя студента №' + str(i + 1) + ' : '
#     input_text_age = 'Введите возраст студента № ' + str(i + 1) + ' : '
#     input_text_average_rating = 'Введите средний бал студента № ' + str(i + 1) + ' : '
#     name = input(input_text_name)
#     age = input(input_text_age)
#     average_rating = input(input_text_average_rating)
#     student['Student ' + str(i + 1)] = {
#       'name': name,
#       'age': age,
#       'average_rating': average_rating
#     }
#     i += 1
# i = 0
# while i < student_count:
#     student_number = 'Student ' + str(i + 1)
#     print('\n' + student_number + ' : ')
#     for key, val in student[student_number].items():
#         print(str(key) + ' - ' + str(val))
#     i += 1
# print(student)

#  Код нормального человека
# school = {'name': ['ivan', 'sergey', 'lena', 'pasha'], 'age': [12, 15, 13, 16], 'average': [3, 4, 2, 5]}
# for key, value in school.items():
#     print ('В ключе - ', key, ' находятся такие значения: ', school[key])
# endregion
# region task2
# dictionary = {(0, 0): 'Настя', (0, 1): 'Святослав', (1, 0): 'Егор'}
# for key,val in dictionary.items():
#     print(str(key) + ' - ' + val)
# endregion
# region task3
# dictionary = {}
# dictionary = {a: a**2 for a in range(8)}
# for i in range(8):
#     dictionary.update({i: i**2})
# print(dictionary)
# endregion
# region task4
# data = [
# {'uuid': 0, 'nik': 'alex', 'years': 13},
# {'uuid': 1, 'nik': 'fred', 'birthday': 15},
# {'uuid': 1, 'nik': 'joy', 'birthday': 8},
# {'uuid': 3, 'nik': 'lily', 'birthday': 5},
# {'uuid': 4, 'nik': 'moo', 'birthday': 9},
# {'uuid': 1, 'nik': 'jack', 'birthday': 10},
# ]

# print(data)
# new_data = {d['uuid']: d for d in data}
# print(new_data)
#
# d1 = {(x, y): x + y for x, y in zip('abc', '123')}
# print(d1)
#
# # имеем список
# lst = [9, 13, 1, 3, 7, 3, 1, 1, 7, 1, 7, 9]
# # создаем ключи будущего словаря (множество set()
# # может иметь только уникальные элементы)
# key = set(lst)
# # создаем словарь `rez` из списка ключей `key`
# # со значением по умолчанию = 0
# rez = dict.fromkeys(key, 0)
# # {1: 0, 3: 0, 7: 0, 9: 0, 13: 0}
# print(key)
# for key in lst:
#     # увеличиваем счетчик
#     # соответствующего ключа на 1
#     rez[key] += 1
#
# # смотрим результат
# print(rez)
# список элементов, которые будут ключами
# key = ['one', 'two', 'three', 'four', 'five']
# # список элементов, которые будут значениями словаря
# value = [1, 2, 3, 4, 5]
# lst = zip(key, value)
# lst1 = list(lst)
# print(lst1)
# # создаем словарь из двух списков
# a = {k: v for k, v in key}
# print(a)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# keys = [a for a in range(1, 6)]
# val = [a**3 for a in keys]
# dictionary1 = {'name': 'alex', 'age': '18'}
# dictionary2 = dict({k: v for k, v in zip(keys, val)})
# dictionary3 = dict.fromkeys(keys, 0)
# for key, val in dictionary1.items():
#     print(f'{key} - {val}')
# for key, val in dictionary2.items():
#     print(f'{key} - {val}')
# for key, val in dictionary3.items():
#     print(f'{key} - {val}')
# endregion
# region task5
# d = {"Один": "Питон", "Два": "C++", "Три": "Java", "Четыре": "C#"}
# d_copy = d.copy()
# del d
# d_copy.pop('Три')
# d_copy.update({'Новое': 'Kotlin'})
# print(d_copy)
# endregion
