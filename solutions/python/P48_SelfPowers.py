def self_power_series(limit):
    return sum(i**i for i in range(1, limit+1))

def problem48():
    return self_power_series(1000) % (10**10)

if __name__ == "__main__":
    print("Solution:", problem48())
