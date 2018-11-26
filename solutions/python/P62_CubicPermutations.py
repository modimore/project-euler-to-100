# from eutil.sequences import unique_permutations
# 
# def is_cubic(x):
#     return x == round(x**(1/3)) ** 3
# 
# def solve(n_permutations=5):
#     x = int(10 ** (n_permutations/3))
#     while True:
#         x3 = x**3
#         s_x = str(x3)
#         cubic_permutations = set()
#         for s_p in unique_permutations(s_x):
#             if s_p[0] == "0":
#                 continue
#             p = int("".join(s_p))
#             if is_cubic(p):
#                 if p < x3:
#                     break
#                 cubic_permutations.add(p)
#         if len(cubic_permutations) == n_permutations:
#             return x3
#         x += 1

def solve(n_permutations=5):
    x = int(10 ** (n_permutations/3))
    log10_current = n_permutations
    permutations_by_sorted_digits = {}
    while True:
        x3 = x**3
        sx3 = "".join(sorted(str(x3)))
        
        if len(sx3) > log10_current:
            candidates = []
            for perms in permutations_by_sorted_digits.values():
                if len(perms) == n_permutations:
                    candidates.append(min(perms))
            if len(candidates) != 0:
                return min(candidates)
            permutations_by_sorted_digits = {}
            log10_current = len(sx3)
        
        if sx3 in permutations_by_sorted_digits:
            permutations_by_sorted_digits[sx3].append(x3)
        else:
            permutations_by_sorted_digits[sx3] = [x3]
        
        x += 1
    
if __name__ == "__main__":
    from sys import argv
    
    N = 5
    if len(argv) > 1:
        try:
            N = int(argv[1])
        except:
            pass
    print("Solution:", solve(N))
