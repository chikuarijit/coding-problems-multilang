def swap(a, b):
    return b, a

def swap2(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a, b = swap(a, b)
print(f"After swapping: a = {a}, b = {b}")
a, b = swap2(a, b)
print(f"After swapping: a = {a}, b = {b}")