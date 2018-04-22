MAX = 4E6

# Just for reference
# def fib(n):
#     return 1 if n < 2 else fib(n-1) + fib(n-2)

result = 0
fib0 = 1
fib1 = 1
while fib1 < MAX:
    if fib1 % 2 == 0:
        result += fib1
    fib0, fib1 = fib1, fib0 + fib1
print(result)
