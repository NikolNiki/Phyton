def average ( a,b ,c ):
    result = (a +b + c) / 3
    return round(result, 2)
print(average(5,7,9))
def foo(something) -> bool:
    return something % 2 == 0 and something > 10

print(foo(12))
print(foo(7))

def count_vowels(text:str) -> int:
    vowels = "aeiouyAEIOUY"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))

