"""Project Euler Solutions
Problem 59: XOR decryption
Solved by: Quinn Mortimer (modimore)
"""
ord_space = ord(b" ")

def xor_encrypt(plain, key):
    key_len = len(key)
    enc = bytearray(len(plain))
    for i, c in enumerate(plain):
        enc[i] = c ^ key[i % key_len]
    return bytes(enc)

def read_input(f):
    with open(f, "rb") as f:
         return f.read()

def sort_by_freq(b):
    freq = {c: b.count(c) for c in b}
    by_freq = list(sorted(((c, f) for c, f in freq.items()), key=lambda p: p[1], reverse=True))
    return bytes([p[0] for p in by_freq])

def solve(filename="P059_Data.bin", key_length=3):
    b = read_input(filename)
    
    key = bytearray(key_length)
    for i in range(key_length):
        key[i] = sort_by_freq(b[i::key_length])[0] ^ ord_space
    
    dec = xor_encrypt(b, bytes(key))
    return sum(int(x) for x in dec)

if __name__ == "__main__":
    print(solve())
