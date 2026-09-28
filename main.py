# 1
# def show_arguments(func):
#     def inner(a, b):
#         print("Arguments:", a, b)
#         return func(a, b)
#     return inner
# @show_arguments
# def multiply(a, b):
#     return a * b
# a = int(input())
# b = int(input())
# print(multiply(a, b))

# 2
# def frame(func):
#     def inner(text):
#         print("=" * 10)
#         result = func(text)
#         print(result)
#         print("=" * 10)
#         return result
#     return inner
# @frame
# def show_text(text):
#     return text
# text = input()
# show_text(text)

# 3
# def double_result(func):
#     def inner(number):
#         return func(number) * 2
#     return inner
# @double_result
# def get_number(number):
#     return number
# number = int(input())
# print(get_number(number))

# 4
# multiply = lambda a, b: a * b
# a = int(input())
# b = int(input())
# print(multiply(a, b))

# 5
# def count_calls(func):
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         print("Call:", count)
#         return func()
#     return inner
# @count_calls
# def hello():
#     print("Hello")
# hello()
# hello()
# hello()

# 6
# def string_only(func):
#     def wrapper(value):
#         if type(value) == str:
#             func(value)
#         else:
#             print("A string is required")
#     return wrapper
# @string_only
# def show(value):
#     print(value)
# show("Hello")


# 7
# def adult_only(func):
#     def wrapper(age):
#         if age < 18:
#             print("Access denied")
#         else:
#             func(age)
#     return wrapper
# @adult_only
# def enter_club(age):
#     print("Welcome")
# age1 = int(input())
# enter_club(age1)
# age2 = int(input())
# enter_club(age2)


# 8
# students = [('Ali', 75), ('Sara', 92), ('Bob', 84)]
# result = sorted(students, key=lambda student: student[1], reverse=True)
# print(result)

# 9
# def add_prefix(func):
#     def wrapper(name):
#         return f"Result: {func(name)}"
#     return wrapper
# @add_prefix
# def get_name(name):
#     return name
# name = input()
# print(get_name(name))


# 10
# def check_division(func):
#     def wrapper(a, b):
#         if b == 0:
#             print("Cannot divide by zero")
#         else:
#             result = func(a, b)
#             print(result)
#     return wrapper
# @check_division
# def divide(a, b):
#     return a / b
# a = int(input())
# b = int(input())
# divide(a, b)


# 11
# numbers = [-4, 7, 0, -2, 9, 3]
# result = list(filter(lambda x: x > 0, numbers))
# print(result)

# 12