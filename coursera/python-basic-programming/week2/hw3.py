# Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).
# Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для решения этой задачи?

a = int(input())
b = int(input())
c = int(input())

max = a

if b > max:
    max = b

if c > max:
    max = c

    if b > c:
        max = b

print(max)