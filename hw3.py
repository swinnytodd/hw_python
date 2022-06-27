#!usr/bin/env python3


def max_list(name):
    name = name.lower()
    name = name.split()
    name.sort()
    count = []
    tmp = " "
    for i in name:
        if i != tmp:
            count.append(name.count(i))
            tmp = i
        else:
            count.append(0)
    for i in range(len(name)):
        if count[i] == max(count):
            print(str(max(count)) + " - " + name[i])


while True:
    inp = input("Input: ")
    if len(inp) == 0:
        break
    else:
        max_list(inp)
print("Exit")