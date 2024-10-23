import random #BONUS

pole = [10, 85, 20, 31, 22, 43, 71, 8, 6] #ukol 1

first_hodnota = pole[0]
middle_hodnota = pole[len(pole)//2]
last_hodnota = pole[-1]

print("První hodnota:", first_hodnota)
print("Prostřední hodnota:", middle_hodnota)
print("Poslední hodnota:", last_hodnota) #ukol 2

pole[5] = 34 #ukol 3
print(pole)

sedma_hodnota = pole[7]

print("7. hodnota:", sedma_hodnota) #ukol 4

print(len(pole)) #ukol 5


print(min(pole))
print(max(pole)) #ukol 6

druhe_pole = [5, 34, 5, 8, 9, 13, 56, 10, 22]
print(druhe_pole) #ukol 7

soucet = sum(druhe_pole)  # součet ukol 8
print("Součet pole:", soucet)

soucet2 = druhe_pole[1] + druhe_pole[5] #ukol 9
print("Součet hodnot (2 Pole) 1 a 5 je:", soucet2)

random.shuffle(druhe_pole) #BONUS

print("Zamíchané pole:", druhe_pole)