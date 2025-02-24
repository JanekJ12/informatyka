def suma_cyfr(liczba):
    suma = 0
    for cyfra in str(liczba):
        suma += int(cyfra)
    return suma

def pierwsza(liczba):
    if liczba < 2:
        return False
    if liczba % 2 == 0 and liczba != 2:
        return False
    for i in range(3, int(liczba**0.5)+1, 2):
        if liczba % i == 0:
            return False
    return True

def czy_trojkat_prostokatny(a, b, c):
    a, b, c = sorted([int(a), int(b), int(c)])
    return a**2 + b**2 == c**2

lista_trojek = []
with open("C:/Users/jan.jurczuk/Documents/GitHub/informatyka/zadania/trojki.txt") as plik:
    for linia in plik:
        lista_trojek.append(linia.split())

print(lista_trojek)

for liczby in lista_trojek:
    if suma_cyfr(liczby[0]) + suma_cyfr(liczby[1]) == int(liczby[2]):
        print(liczby)

for liczby in lista_trojek:
    if int(liczby[0]) + int(liczby[1]) == int(liczby[2]):
        if pierwsza(int(liczby[0])) and pierwsza(int(liczby[1])):
            print(liczby)

for i in range(len(lista_trojek) - 1):
    wiersz1 = lista_trojek[i]
    wiersz2 = lista_trojek[i + 1]
    for j in range(len(wiersz1) - 2):
        if czy_trojkat_prostokatny(wiersz1[j], wiersz1[j+1], wiersz1[j+2]):
            print("+" + " ".join(wiersz1))
            print("=" + " ".join(wiersz2))
