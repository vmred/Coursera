# В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения
# (для решения задачи разрешается использовать числа с запятой).

# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.

# Формат ввода
# Программа получает на вход числа x и y.

# Формат вывода
# Программа должна вывести одно натуральное число.

x = int(input())
y = int(input())

d = 1

while x < y:
    x += x * 0.1
    d += 1

print(d)
