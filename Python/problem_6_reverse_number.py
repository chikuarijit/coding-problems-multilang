def reverse(num):
    result = 0
    temp = 0
    while(num > 0):
        temp = num % 10
        result = (result * 10) + temp
        num = num//10

    return result



num = int(input("Enter a number: "))
print(f"Reverse of {num} is: {reverse(num)}")