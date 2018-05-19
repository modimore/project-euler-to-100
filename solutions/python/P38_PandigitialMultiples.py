best = 0
all_digits = {x for x in range(1,10)}
for n in range(1, 9876):
    m = 1
    concat_prods = ""
    digits_seen = set()
    while len(all_digits - digits_seen) > 0 and len(digits_seen) == len(concat_prods):
        prod = n * m
        s_prod = str(prod)
        concat_prods += s_prod
        digits_seen |= {int(d) for d in s_prod}
        m += 1
    if len(digits_seen) == len(concat_prods) and 0 not in digits_seen:
        best = max(best, int(concat_prods))

print(best)
