from eutil.numbers import digit_list

N = 1000000

def is_palindrome(n, base=10):
    digits = digit_list(n, base)
    for i in range(len(digits)//2):
        if digits[i] != digits[-i-1]:
            return False
    return True

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        try: N = int(sys.argv[1])
        except ValueError:
            print("Could not parse argument as integer")
    
    twobase_palindrome_sum = 0
    for n in range(N):
        if is_palindrome(n, 10) and is_palindrome(n, 2):
            twobase_palindrome_sum += n
    
    print(twobase_palindrome_sum)
