# По данному целому числу N распечатайте все квадраты натуральных чисел,не превосходящие N, в порядке возрастания.

# Формат ввода
# Вводится натуральное число.

# Формат вывода
# Выведите ответ на задачу.

value = int(input())

i = 1
while i <= value:
    q = i ** 2
    if q <= value:
        print(q, end=' ')
    i += 1