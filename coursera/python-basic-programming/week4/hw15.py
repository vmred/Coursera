# Для быстрого вычисления наибольшего общего делителя двух чисел используют алгоритм Евклида.
# Он построен на следующем соотношении: НОД(a,b)=НОД(b,a % b).


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(int(input()), int(input())))