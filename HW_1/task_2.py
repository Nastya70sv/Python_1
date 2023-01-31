# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input("Enter a number from 100 to 999 : "))
print(a)
sum = 0
if a > 999 or a < 100:
    print (f' This number {a} is not in the interval from 100 to 999')
else:
    print (f' This number {a} is the interval from 100 to 999')
    while a > 0 :
            sum += a % 10
            a //= 10
    print((f'Sum of 3 numbers = {sum}'))
       

    