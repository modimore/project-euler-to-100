from eutil.primes import primes, primes_below, get_primes_fast

limit = int(1E6)

"""
def problem50():
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
        while 0 < j:
            run_sum += sorted_primes[j]
            run += 1
            if run_sum < limit and run_sum in s_primes:
                local_best_run_sum = run_sum
                local_best_run = run
            j -= 1
        if local_best_run > best[1]:
            best = (local_best_run_sum, local_best_run)
        i += 1
    return best[0]
"""
def problem50():
    s_primes = get_primes_fast(limit)
    sorted_primes = sorted(s_primes)
    best = (None, 0)
    i = 0
    while i < len(sorted_primes):
        p = sorted_primes[i]
        print(p)
        if p >= limit:
            break
        run_sum = p
        run = 1
        local_best_run_sum = run_sum
        local_best_run = run
        j = i-1
        if j%2 == 1:
            run_sum += sorted_primes[j]
            run += 1
            j -= 1
        while 0 < j:
            run_sum += sorted_primes[j] + sorted_primes[j-1]
            run += 2
            if run_sum < limit and run_sum in s_primes:
                local_best_run_sum = run_sum
                local_best_run = run
            j -= 2
        if run_sum + 2 in s_primes:
            local_best_run_sum += 2
            local_best_run += 1
        if local_best_run > best[1]:
            best = (local_best_run_sum, local_best_run)
        i += 1
    return best[0]
"""
def problem50():
    best = (None, 0)
    i = 0
    running_sum = 0
    while True:
        p = primes[i]
        if p >= limit:
            break
        running_sum += p
        local_best = running_sum
        j = -1
        while local_best > limit or local_best not in primes:
            j += 1
            local_best -= primes[j]
        if i-j > best[1]:
            best = (local_best, i-j)
        i += 1
    return best[0]
"""

if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        try: limit = int(argv[1])
        except ValueError: print("Could not parse argument as integer.")
    print("Solution:", problem50())
