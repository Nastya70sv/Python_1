# Дана последовательность из N целых чисел и число K.
#  Необходимо сдвинуть всю последовательность (сдвиг - циклический)
#   на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 2

# Output: [4, 5, 1, 2, 3]

# решение №1 
list_1 = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(list_1)
list_result = list()

for i in range(k):
    list_result.append(list_1[len(list_1) - k + i])

for i in range(len(list_1) - k):
    list_result.append(list_1[i])
print(list_result)

# решение №2
# lst = [1, 2, 3, 4, 5]
# k = int(input())
# k %= len(lst)

# for i in range(k):
#     lst.insert(0, lst.pop(len(lst)-1))
# print(lst)