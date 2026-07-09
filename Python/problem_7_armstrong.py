def is_armstrong(n):
    num = n
    num_list = []
    while n:
        temp = n % 10
        num_list.append(temp)
        n = n // 10

    armstrong = sum([i ** len(num_list) for i in num_list])
    return armstrong == num

n = int(input("Enter a number to check if it is an Armstrong number: "))
print(is_armstrong(n))