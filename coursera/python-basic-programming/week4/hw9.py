# Дано натуральное число n>1. Выведите его наименьший делитель, отличный от 1.
# Решение оформите в виде функции MinDivisor(n).
# Алгоритм должен иметь сложность порядка корня квадратного из n.
#
# Указание. Если у числа n нет делителя не превосходящего корня из n,
# то число n — простое и ответом будет само число n.
# А у всех составных чисел обязательно есть делители,
# отличные от единицы и не превосходящие корня из n.


def MinDivisor(n):
    for i in range(2, n + 1):
        if i > n ** 0.5:
            return n
        if not n % i:
            return i


print(MinDivisor(int(input())))
