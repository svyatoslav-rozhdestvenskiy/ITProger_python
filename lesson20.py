# region lesson20
# import webbrowser
#
#
# def validator(func):
#     def wrapper(url):
#         if "." in url:
#             func(url)
#         else:
#             print("Неверный URL")
#
#     return wrapper
# @validator
# def open_url(url):
#     webbrowser.open(url)
# open_url("https://itproger.com")
# endregion
# region task1
# def decorator(func):
#     def wrapper(a, b):
#         print("Код до выполнения функции")
#         func(a, b)
#         print("Код после выполнения функции")
#     return wrapper
#
#
# @decorator
# def summa(a, b):
#     print(a + b)
#
#
# summa(3, 4)
# endregion