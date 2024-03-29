# Дана последовательность натуральных чисел x₁ x₂ ..., xn.
# Стандартным отклонением называется величина
# σ=sqrt(((((x₁-s)²+(x₂-s)²+…+(xn-s)²) / (n-1))))

# где s = ((x₁+x₂+…+xn) / n) — среднее арифметическое последовательности, а sqrt - квадартный корень.
# Определите стандартное отклонение для данной последовательности натуральных чисел,завершающейся числом 0.

# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся числом 0
# (само число 0 в последовательность не входит, а служит как признак ее окончания).

# Формат вывода
# Выведите ответ на задачу.

s = 0
n = 0
kv_summ = 0

while True:
    value = int(input())
    if value == 0:
        break

    s += value
    kv_summ += value ** 2
    n += 1

k = s / n

print(((kv_summ - 2 * k * s + n * k ** 2) / (n - 1)) ** 0.5)
