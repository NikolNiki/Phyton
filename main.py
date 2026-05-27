<<<<<<< HEAD
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
from functions import calculate, change_text, sum_numbers

# 1. Позиционные аргументы

print(calculate(10,5))
print(change_text("hello"))
print(sum_numbers("1,2,3"))

# 2. Именованные аргументы

print(calculate(a=10, b=5, operation="sub"))

print(change_text(text="Hello", upper=False))

print(sum_numbers("1,2,3,4"))

# 3. Через **dick

data1 = {
    "a": 20,
    "b": 5,
    "operation": "sub"
}

print(calculate(**data1))

data2 = {
    "text": "Python",
    "upper": True
}

print(change_text(**data2))

data3 = {
    "numbers": "10,20,30",
    "separator": ","
}

print(sum_numbers(**data3))
>>>>>>> origin/main
