# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

monets = int(input(" How many coins do you have ? "))
count = 0
eagle = 0
tails = 0
for i in range(monets) :
    print()
    print(f" Coin number {i+1} ")
    mas = int (input( "The coin is eagle, if yes enter 1, if not enter 0 : "))
    if mas == 0 :
        eagle += 1 
    elif mas == 1 :
        tails += 1
if eagle > tails :
    print()
    print (f' You need to flip {tails} eagle')
else:
    print()
    print (f' You need to flip {eagle} tails')
