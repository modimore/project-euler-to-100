"""Project Euler Solutions
Problem 19: Counting Sundays
Solved by: Quinn Mortimer (modimore)
"""
jan_1_1901 = 2
current_day = jan_1_1901

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_per_month_leap_year = days_per_month[:]; days_per_month_leap_year[1] = 29

sunday_the_firsts = 0
for year in range(1901, 2001):
    curr_days_per_month = days_per_month_leap_year if year % 4 == 0 else days_per_month
    
    for days in curr_days_per_month:
        if current_day % 7 == 0:
            sunday_the_firsts += 1
        current_day += days

print(sunday_the_firsts)
