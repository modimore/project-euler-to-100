MAX_POWER = 6
target_digits = [10**n for n in range(MAX_POWER+1)]
target_digits.append(None)

total_len = 0
num = 1
product = 1
target_digit = target_digits.pop(0)
while len(target_digits) > 0:
    s_num = str(num)
    total_len += len(s_num)
    
    if target_digit <= total_len:
        d = s_num[target_digit - (total_len-len(s_num)) - 1]
        product *= int(d)
        target_digit = target_digits.pop(0)
    
    num += 1

print(product)
