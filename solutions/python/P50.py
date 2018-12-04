"""Project Euler Solutions
Problem 50: Consecutive prime sum
Solved by: Quinn Mortimer (modimore)
"""
from eutil.primes import get_primes_fast

L = int(1E6)

def problem50(limit=L):
    s_primes = get_primes_fast(limit)
    sorted_primes = sorted(s_primes)
    best = (None, 0)
    i = 0
    while i < len(sorted_primes):
        p = sorted_primes[i]
        if p >= limit:
            break
        run_sum = p
        run = 1
        local_best_run_sum = run_sum
        local_best_run = run
        j = i-1
        while 0 <= j:
            run_sum += sorted_primes[j]
            run += 1
            if run_sum < limit and run_sum in s_primes:
                local_best_run_sum = run_sum
                local_best_run = run
            if run_sum >= limit:
                break
            j -= 1
        if local_best_run > best[1]:
            best = (local_best_run_sum, local_best_run)
        i += 1
    return best[0]

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        try: L = int(argv[1])
        except ValueError: print("Could not parse argument as integer.")
    print(problem50(L))
