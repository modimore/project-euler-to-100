"""Project Euler Solutions
Problem 17: Number letter counts
Solved by: Quinn Mortimer (modimore)
"""
number_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
   10: "ten",
   11: "eleven",
   12: "twelve",
   13: "thirteen",
   14: "fourteen",
   15: "fifteen",
   16: "sixteen",
   17: "seventeen",
   18: "eighteen",
   19: "nineteen",
   20: "twenty",
   30: "thirty",
   40: "forty",
   50: "fifty",
   60: "sixty",
   70: "seventy",
   80: "eighty",
   90: "ninety"
}

number_components = {
  100: ("hundred", "and"),
 1000: ("thousand", None)
}

def get_natural_language_number(n):
    if n in number_words:
        return number_words[n]
    
    n_word = ""
    for k in sorted(number_components.keys(), reverse=True):
        if n < k: continue
        
        rem = n % k
        big_dig = (n - rem) // k
        
        k_comp = number_components[k]
        big_dig_comp = get_natural_language_number(big_dig)\
                     + k_comp[0]
        
        n_word += big_dig_comp
        if rem > 0:
            n_word += (" " + k_comp[1] + " ") if k_comp[1] is not None else ""
            n = rem
        else:
            break

def get_natural_language_number2(n):
    
    n_word = ""
    splitter_keys = sorted(number_components.keys())
    min_splitter = splitter_keys[0]
    while len(splitter_keys) > 0:
        key = splitter_keys.pop()
        rem = n % key
        big = n - rem
        n = rem
        
        if big == 0: continue
        
        big_dig = big // key
        n_word += get_natural_language_number2(big_dig) + " "
        splitter = number_components[key]
        n_word += splitter[0]
        if splitter[1] is not None and n > 0:
            n_word += " " + splitter[1] + " "
        elif n > 0:
            n_word += " "
    
    if n == 0:
        return n_word
    
    if n in number_words:
        n_word += number_words[n]
    else:
        n_1 = n % 10
        n_10 = n - n_1
        n_word += number_words[n_10] + " " + number_words[n_1]
    
    return n_word

tot_len = 0
for i in range(1, 1001):
    n_word = get_natural_language_number2(i)
    print(n_word)
    tot_len += sum(1 for c in n_word if not c.isspace())
print(tot_len)
