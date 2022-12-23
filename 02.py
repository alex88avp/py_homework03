# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
list = [randint(0, 10) for i in range(randint(5, 10))]
print(list)
mult = []
length = len(list)
mid = length//2 + length % 2
for i in range(mid):
    mult.append(list[i] * list[length - i -1])
print(mult)