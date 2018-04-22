def generate_collatz_sequence(n):
    if n <= 0:
        return []

    seq = [n]
    curr = n
    while curr != 1:
        if curr % 2 == 0:
            curr = curr //2
        else:
            curr = 3 * curr + 1
        
        seq.append(curr)

    return seq


if __name__ == "__main__":
    best = (0,0)
    key = lambda p: p[1]
    for i in range(1, 1000000):
        best = max(best, (i,len(generate_collatz_sequence(i))), key=key)

    print("Longest:", best[0], "@", best[1])
