# Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов.
# Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами
# также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего пингвина.
# Для упрощения рисования скопируйте пингвина из примера в среду разработки.

value = int(input())

a = "   _~_    "
b = "  (o o)   "
c = " /  V  \\  "
d = "/(  _  )\\ "
e = "  ^^ ^^   "

print(a * value)
print(b * value)
print(c * value)
print(d * value)
print(e * value)
