# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# 1 решение
# list_1 = [1, 1, 2, 3, 0, -4, 4, 4]
# print(len(set(list_1)))

# 2 решение

list_1 = [1, 1, 2, 2, 3, 3, 4, 4]
result_list = list()
for i in list_1:
    if i not in result_list:
        result_list.append(i)
print(result_list)
print(len(result_list))