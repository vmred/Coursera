# Решить в целых числах уравнение: (ax+b) / (cx+d) =0

# Формат ввода
# Вводятся 4 числа: a,b,c,d; c и d не равны нулю одновременно.

# Формат вывода
# Необходимо вывести все решения, если их число конечно, “NO” (без кавычек), если решений нет,
# и “INF” (без кавычек), если решений бесконечно много.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    print('INF')
else:
    if a == 0 or b % a != 0 or c * (-b / a) + d == 0:
        print('NO')
    else:
        print(int(-b / a))
