#!/usr/bin/env python3
input_list = input().split()
buff = {}
res_list = " ".join([buff.setdefault(x, x) for x in input_list if x not in buff])
print(res_list)