string = '"fddfs456"'

d = {'Спец.символы': 0, 'Буквы': 0, 'Цифры': 0}
for i in string:
    if i.isalpha():
        d['Буквы'] += 1
    elif i.isdigit():
        d['Цифры'] += 1
    else:
        d['Спец.символы'] += 1

print(d['Цифры'], d['Буквы'], d['Спец.символы'])