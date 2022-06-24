#!/usr/bin/env python3

def find_steps(number, ctr):
    if number == 1:
        print(ctr)
        return
    if number % 2 == 0:
        find_steps(number // 2, ctr + 1)
    else:
        find_steps(number * 3 + 1, ctr + 1)


# range 1 ,100
for i in range(1, 100, 10):
    n = 0
    find_steps(i, n)