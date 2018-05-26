from eutil.numbers import primes

def reconstruct_from_digits(digits):
    value = 0
    for d in digits:
        value = value * 10 + d
    return value

def is_substring_divisible(digits):
    for i in range(1, len(digits)-2):
        value = reconstruct_from_digits(digits[i:i+3])
        if value % primes[i-1] != 0:
            return False
    return True

if __name__ == "__main__":
    from itertools import permutations
    
    total = 0
    for p in permutations(tuple([0,1,2,3,4,5,6,7,8,9])):
        if is_substring_divisible(p):
            total += reconstruct_from_digits(p)
    
    print(total)
