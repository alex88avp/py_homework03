# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def frac(number):
    return round(number % 1, 2)


list = [round(random.uniform(0, 10), 2) for i in range(random.randint(2, 8))]
print(list)
listFrac = []
for i in list:
    if i%1 !=0:
        listFrac.append(frac(i))
print(listFrac)

max = listFrac[0]
min = listFrac.pop(0)
for i in listFrac:
    if i > max:
        max = i
    elif i < min:
        min = i
print(f'Разница между макс и мин значениями дробной части равна {max - min}')