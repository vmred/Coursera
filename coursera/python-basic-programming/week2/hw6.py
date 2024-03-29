# В доме несколько подъездов.
# В каждом подъезде одинаковое количество квартир.
# Квартиры нумеруются подряд, начиная с единицы.
# Может ли в некотором подъезде первая квартира иметь номер x, а последняя – номер y?

# Формат ввода
# Вводятся два натуральных числа x и y (x ≤ y), не превышающие 10000.

# Формат вывода
# Выведите слово YES (заглавными латинскими буквами), если такое возможно, и NO в противном случае.


x = int(input())
y = int(input())

print('YES' if y % (y - x + 1) == 0 else 'NO')
