def find_triple(n):
    a, b, c = 0, 0, n//2
    c_min = n // 3

    while c > c_min:
        b = 0
        while b < c:
            a = 0
            while a <= b:
                if a + b + c == n:
                    a2b2 = a**2 + b**2
                    c2 = c**2
                    if a2b2 == c2:
                       return a, b, c
                    elif a2b2 > c2:
                        a = b = c
                a += 1
            b += 1
        c = c-1

    return None

print(find_triple(1000))
