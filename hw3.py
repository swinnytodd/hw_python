#!usr/bin/env python3


list_input = [x.lower() for x in input().split()]
dict = {}
max_val = 0

for el in list_input:
    if list_input.count(el) >= max_val:
        max_val = list_input.count(el)
        dict[el] = list_input.count(el)

for key in dict:
    if dict[key] == max_val:
        print(str(max_val) + ' ' + key)