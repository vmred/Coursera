# Напишите функцию xor(x, y)
# реализующую функцию "Исключающее ИЛИ" двух логических переменных x и y.
# Функция xor должна возвращать True, если ровно один из ее аргументов x или y,
# но не оба одновременно равны True


def xor(x, y):
    return int(bool(x) != bool(y))


print(xor(int(input()), int(input())))