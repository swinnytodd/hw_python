#!/usr/bin/env python3

sum_ = 0
for i in range(0, 1000001):
    if str(i)[::-1] == str(i) and "{0:b}".format(i)[::-1] == "{0:b}".format(i):
        sum_ += i
print("Sum =", sum_)