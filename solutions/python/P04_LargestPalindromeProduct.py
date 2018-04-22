# Project Euler Problem 4

# It turns out that it is not safe to assume that the maximum product is
# the first palindromic product reached, though I have not figured out
# what a suitable point to cut off the search is short of reaching 2 digit
# numbers.

def is_number_palindrome(n, radix=10):
    nrev, tmp = 0, n
    while tmp > 0:
        nrev = nrev * radix + tmp % radix
        tmp //= radix
    
    return nrev == n

# Any actual result will be positive, as x > 0, y > 0 -> x * y > 0
result = 0
for i in range(999, 99, -1):
    for j in range(999, i, -1):
        product = i * j
        if is_number_palindrome(product):
            result = max(result, product)

print(result)
