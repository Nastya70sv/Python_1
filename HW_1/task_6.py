# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

A = int(input( "Введите первые три числа билета : "))
S = A
print(S)
sum1 = 0 
while S > 0 :
    sum1 += S % 10
    S //= 10
print(sum1)    
B = int(input( "Введите последующие три числа билета : "))
P = A
print(P)
sum2 = 0 
while P > 0 :
    sum2 += P % 10
    P //= 10
print(sum2) 
if sum1 == sum2:
    print(f'Ура билетик под номером №{A}{B} СЧАСТЛИВЫЙ')
else:
    print(f'Билет под номером №{A}{B} НЕ счастливый')



# второй вариант решения, более простой
# bilet = (input('Введите шестизначный номер на билетике: '))
# onesum = int(bilet[0]) + int(bilet[1]) + int(bilet[2])
# twosum = int(bilet[3]) + int(bilet[4]) + int(bilet[5])
# if onesum == twosum:
#     print(f'Билетик под номером №{bilet} - является счастливым :D')
# else:
#     print(f'Билетик под номером №{bilet} - не является счастливым!')
