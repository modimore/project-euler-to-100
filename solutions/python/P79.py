"""Project Euler Solutions
Problem 79: Passcode derivation
Solved by: Quinn Mortimer (modimore)
"""
import itertools

def helper(codes):
    """Basically, there is a set of characters we know are
    in the password, with some ordering relationship, and an alphabet.
    If iterate through all the permuations of the letters we know are
    in the passcode, returning that if it satisfies the known ordering
    conditions, we may eventually find the passcode.
    
    We also may not, in which case we should progressively add more and
    more combinations of characters from the alphabet and make permutations
    with those and the known characters. This should be guaranteed to get
    a matching sequence eventually.
    """
    code_chars = set()
    for code in codes:
        code_chars |= set(code)
    
    code_chars = sorted(code_chars)
    # could just be list(code_chars)
    # but it's easier to benchmark if the order is deterministic
    
    alphabet = list(str(x) for x in range(10))
    
    repeat = 0
    while True:
        for extra_chars in itertools.product(alphabet, repeat=repeat):
            for password in itertools.permutations(code_chars + list(extra_chars)):
                password = "".join(password)
                success = True
                for code in codes:
                    i = 0
                    for c in code:
                        i = password.find(c, i)
                        if i == -1:
                            success = False
                            break
                if success:
                    return password
        repeat += 1
    
def solve(filename="P79_Input.txt"):
    codes = []
    with open(filename, "r") as f:
        codes = [line.strip() for line in f]
    return helper(codes)

if __name__ == "__main__":
    print(solve())
