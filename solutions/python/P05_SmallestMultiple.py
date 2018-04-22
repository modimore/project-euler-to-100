import math

NUM = 600851475143

def generate_primes(limit):
    current = 3
    all_primes = [2]
    while current <= limit:
        is_prime = True
        for p in all_primes:
            if current % p == 0:
                is_prime = False
            if p**2 > current:
                break
        if is_prime:
            all_primes.append(current)
        
        # Simplest test available for primeness, but takes a long time
        # if all(current % p_n != 0 for p_n in all_primes):
        #    all_primes.append(current)

        current += 2
    return all_primes

def gcf(a, b):
    while b > 0:
        a, b = b, a%b
    return  a

N = 20

if __name__ == "__main__":
    result = 1
    for i in range(N, 1, -1):
        if result % i != 0:
            result *= i // gcf(result, i)
    
    print("Result:", result)

    print("Valid:", all(result % i == 0 for i in range(1, N+1)))
