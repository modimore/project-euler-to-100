"""Project Euler Solutions
Problem 31: Coin sums
Solved by: Quinn Mortimer (modimore)
"""
def make_change(amount, coins):
    if len(coins) == 0:
        return 0
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    largest_coin = max(coins)
    smaller_coins = set(coins) - { largest_coin }
    return make_change(amount - largest_coin, coins)\
         + make_change(amount, smaller_coins)

print(make_change(200, {1, 2, 5, 10, 20, 50, 100, 200}))
