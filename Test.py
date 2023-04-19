
# Задача:
# Написать программу, которая из имеющегося массива строк сформирует массив строк, длина которых меньше либо равна 3 символа.
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
# При решении не рекомендкется пользоваться коллекциями, лучше обойтись исключительно массивами.

# Пример:
# ["hello", "2", "world", ":-)"] -> ["2",":-)"]

arrayOfStringsIn = ["hello", "2", "world", ":-)"]
arrayOfStringsOut = []
indexOut = 0
limit = 3

for indexIn in range(len(arrayOfStringsIn)):
    if (len(arrayOfStringsIn[indexIn]) <= limit):
        arrayOfStringsOut.append(arrayOfStringsIn[indexIn])
        # arrayOfStringsOut[indexOut] = arrayOfStringsIn[indexIn]
        # indexOut += 1

print(arrayOfStringsOut)

