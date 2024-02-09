# region lesson6
# for i in range(1, 6, 2):
#     print(i)
# count = 0
# word = 'Hello World!'
# for i in word:
#     if i == '!':
#         count += 1
#
# print(count)

# i = 5
# while i < 15:
#     print(i)
#     i += 2

# for i in range(1, 11):
#     if i == 8:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)
# endregion
# region task1
index = 34
while index <= 67:
    if index % 2 != 0:
        index += 1
        continue
    print(index)
    index += 1
# endregion
# region task2
i = 0
while True:
    print (i)
    i += 1
    if i > 5:
        break
# endregion
# region task3
i = 1
while i <= 100:
    if i == 50 or i == 99:
        i += 1
        continue
    print(i)
    i += 1
for i in range (1, 101):
    if i == 50 or i == 99:
        continue
    print(i)
# endregion
# region task4
word = input('Введите слово, которое хотите повторить по буквам: ')

while True:
    repeat_number = input('Введите количество повторений: ')
    try:
        repeat_number = int(repeat_number)
        break
    except ValueError:
        print('Некорректный ввод числа, попробуйте снова')

for char in word:
    print(char * repeat_number)
# endregion
