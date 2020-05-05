"""Project Euler Solutions
Problem 89: Roman numerals
Solved by: Quinn Mortimer (modimore)
"""

RN_DIGITS = [
    ('I', 1),
    ('IV', 4),
    ('V', 5),
    ('IX', 9),
    ('X', 10),
    ('XL', 40),
    ('L', 50),
    ('XC', 90),
    ('C', 100),
    ('CD', 400),
    ('D', 500),
    ('CM', 900),
    ('M', 1000)
]

def read_rn(s):
    i, n = 0, 0
    for dig, val in RN_DIGITS[::-1]:
        l = len(dig)
        while i + l <= len(s) and s.find(dig, i, i+l) == i:
            n += val
            i += l
    return n

def write_rn(val):
    avail = RN_DIGITS[:]
    current = avail.pop()
    s = ""
    while val > 0:
        if current[1] <= val:
            s += current[0]
            val -= current[1]
        else:
            current = avail.pop()
    return s

def solve(filename="P089_Input.txt"):
    char_saved = 0
    for line in open(filename, "r"):
        rn_in = line.strip()
        rn_out = write_rn(read_rn(rn_in))
        char_saved += len(rn_in) - len(rn_out)
    return char_saved
            

if __name__ == "__main__":
    print(solve())
