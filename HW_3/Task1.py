# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.
# *Пример:*
# 5
#     7 -2 3 5 1
#     3
#     -> 1

N = int(input("Введите N: "))

arr = []
for i in range(N):
    arr.append(int(input(f"Введите {i+1} число:")))

search = int(input(f"Введите искомое число:"))
count = 0
for item in arr:
    if item == search:
        count += 1
print(arr)
print("->", count)
