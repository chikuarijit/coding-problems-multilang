def fibo(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    a,b = 0, 1
    series = [a, b]
    for i in range(2, n):
        c = a + b
        series.append(c)
        a, b = b, c
    return series

n = int(input("Enter the number of terms in the Fibonacci series: "))
print(fibo(n))