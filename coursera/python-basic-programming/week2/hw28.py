# Последовательность состоит из натуральных чисел, не превосходящих 10⁹, и завершается числом 0.
# Определите значение наибольшего элемента последовательности.

# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит, а служит как признак ее окончания).

value = -1
m = 0

while value != 0:
    value = int(input())
    m = value if value > m else m

print(m)
