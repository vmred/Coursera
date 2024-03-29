# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определите размер вклада через год.
# При решении этой задачи нельзя пользоваться условными инструкциями и циклами.

# Формат ввода
# Программа получает на вход целые числа P, X, Y.

# Формат вывода
# Программа должна вывести два числа: величину вклада через год в рублях и копейках.
# Дробная часть копеек отбрасывается.

p = float(input())
x = int(input())
y = int(input())

value = (x + y / 100) * pow(1 + p / 100, 1)
value = int(value * 100) / 100
print(' '.join(str(value).split('.')))
