"""Project Euler Solutions
Problem 22: Names scores
Solved by: Quinn Mortimer (modimore)
"""
filename = "P22_Input.txt"

def name_sum(name):
    name_sum = 0
    base = ord("a") - 1
    for char in name.lower():
        name_sum += ord(char) - base
    return name_sum

all_names = []
with open(filename, "r") as f:
    all_names = [name.replace("\"", "") for name in f.readline().split(",")]

all_names = sorted(all_names)

total_score = 0
for index, name in enumerate(all_names):
    total_score += (index + 1) * name_sum(name)

print(total_score)
