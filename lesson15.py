# region lesson15
# try:
#     with open('lesson15/text.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Файл не найден")
# endregion
# region task_1_2
with open('lesson15/test1.txt', 'w') as file:
    file.write("Наш новый файл\n")
with open('lesson15/test1.txt', 'r') as file:
    information = file.read()
    print(information)
# endregion