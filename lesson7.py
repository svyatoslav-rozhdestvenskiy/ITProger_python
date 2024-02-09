# region lesson7
# nums = [1, 2, 3, 4, 5, True, 'Hello', 6.7, [5, 7]]
# nums[0] = 50
# nums[5] = 1.01
# print(nums[-1][0])
#
# numbers = [5, 2, 7]
# numbers.append(100)
# numbers.insert(1, True)
# b = [5, 6, 8]
# numbers.extend(b)
# numbers.sort()
# numbers.reverse()
# numbers.pop(0)
# numbers.remove(5)
# print(numbers.count(5))
# print(numbers)
# print(len(numbers))
#
# nums = [5, 2, 7, '50', False]
# for el in nums:
#     print(el)
# while True:
#     n = input('Введите количество элементов массива: ')
#     try:
#         n = int(n)
#         break
#     except ValueError:
#         print('Некорректный ввод числа, попробуйте снова')
# user_list = []
# i = 0
# while i < n:
#     string = 'Введите элемент массива №' + str(i+1) + ': '
#     user_list.append(input(string))
#     i += 1
# print(user_list)
# endregion
# region task1
# list1 = []
# for i in range(5):
#     list1.append(i)
# print(list1)
# list2 = []
# list2 += [5]
# list2 += [-6]
# list2.extend(list1)
# list2.sort()
# print(list2)
# endregion
# region task2
# list1 = []
# word = input("Введите строку : ")
# for i in range(len(word)):
#     list1.append(word[i])
# print(list1)
# endregion
# region task3
# lis = ['Андрей', "Иван", 'Василий', 'Петро', 'Максим', 'Дима']
# for index in range(len(lis)):
#     word = lis[index]
#     print(word)
#     for char in word:
#         print(char)
# endregion
# region task4
# lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
# min = lis[0]
# for i in lis:
#     if i < min:
#         min = i
# print('Минимальный элемент списка : ' + str(min))
# lis.remove(min)
# if min < 0:
#     lis.append(min)
# else:
#     lis.index(0, min)
# print(lis)
# endregion
# region task5
while True:
    n = input('Введите количество элементов массива : ')
    try:
        n = int(n)
        break
    except ValueError:
        print('Неправильный формат числа')
some = [9, 'Hi', 23.5, 'A']
for i in range(n):
    string = ('Введите элемент массива №' + str(i + 1) + ' : ')
    some.append(input(string))
print(some)
# endregion
