# Даны координаты двух точек на плоскости, требуется определить,
# лежат ли они в одной координатной четверти или нет (все координаты отличны от нуля).

# Формат ввода
# Вводятся 4 числа: координаты первой точки (x1,y1) и координаты второй точки (x2,y2).

# Формат вывода
# Программа должна вывести слово YES, если точки находятся в одной координатной четверти,
# в противном случае вывести слово NO.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print('YES' if x1 * x2 > 0 and y1 * y2 > 0 else 'NO')