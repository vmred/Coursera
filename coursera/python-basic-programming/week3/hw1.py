# Даны длины сторон треугольника. Вычислите площадь треугольника.

# Формат ввода
# Вводятся три положительных числа.

# Формат вывода
# Выведите ответ на задачу.

a, b, c = float(input()), float(input()), float(input())

p = (a + b + c) / 2
print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
