# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3
# -> 1

n = int(input("Enter the length of the array : "))
A = [i for i in range (1, n + 1 )]
print(A)
x = int(input("Enter the number : "))
cnt = 0 
for i in range(n):
    if A[i] == n:
        cnt += 1
print(cnt)