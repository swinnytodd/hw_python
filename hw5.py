#!/usr/bin/env python3

# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.


def negative_num():
    input_list = sorted((int(x) for x in input().split()))
    i = 0

    min_numb = input_list[0]
    if min_numb > 1:
        return min_numb - 1
    while i <= len(input_list):
        if min_numb not in input_list:
            return min_numb


        i += 1
        min_numb += 1


print(negative_num())

