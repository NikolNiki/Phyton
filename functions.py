# functions.py

def calculate(a: int, b: int, operation: str = "sum") -> int:
    if operation == "sub":
        return a - b

    return a + b

def change_text(text: str, upper: bool = True) -> str:
    if upper:
        return text.upper()

    return text.lower()

def sum_numbers(numbers: str, separator: str = ",") -> int:
    parts = numbers.split(separator)

    total = 0

    for num in parts:
        total += int(num)

        return total


