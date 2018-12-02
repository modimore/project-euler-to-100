"""Project Euler Solutions
Problem 61: Cyclical figurate numbers
Solved by: Quinn Mortimer (modimore)
"""
from eutil.numbers import triangle_number, square_number, pentagon_number,\
    hexagon_number, heptagon_number, octagon_number

def make_gen(f, start=0):
    i = start
    while True:
        yield f(i)
        i += 1

def take_while(s, f):
    it = iter(s)
    n = next(it)
    while f(n):
        yield n
        n = next(it)

lt1000 = set(range(1000))
is_4_digit = lambda x: x < int(1E4)
ngonal_numbers = {
        3: set(take_while(make_gen(triangle_number, 1), is_4_digit)),
        4: set(take_while(make_gen(square_number, 1), is_4_digit)),
        5: set(take_while(make_gen(pentagon_number, 1), is_4_digit)),
        6: set(take_while(make_gen(hexagon_number, 1), is_4_digit)),
        7: set(take_while(make_gen(heptagon_number, 1), is_4_digit)),
        8: set(take_while(make_gen(octagon_number, 1), is_4_digit))
}

def solve_helper(start, stop, avail, result=None):
    set_start_stop = set(range(start, stop))
    
    if result is None:
        result = []
    
    for i, n in enumerate(avail):
        n_avail = avail[:i] + avail[i+1:]
        for x in ngonal_numbers[n] & set_start_stop:
            x_start = (x % 100) * 100
            if x_start < 1000:
                continue
            
            if len(avail) > 1:
                for l in solve_helper(x_start, x_start+100, n_avail, result + [x]):
                    yield l
            else:
                if (result[0]//100) == (x % 100):
                    yield result + [x]

def solve():
    for l in solve_helper(int(1E3), int(1E4), [3,4,5,6,7,8]):
        break
    return sum(l)

if __name__ == "__main__":
    print("Solution:",solve())
