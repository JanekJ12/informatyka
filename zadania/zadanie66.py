
def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma
lista_trojek = []
with open("C:/Users/jan.jurczuk/Documents/GitHub/informatyka/zadania/trojki.txt") as pliki:
    for linia in pliki:
        lista_trojek.append(linia.split())
print(lista_trojek)

for liczby in lista_trojek:
    if suma_cyfr(liczby[0]) + suma_cyfr(liczby[1]) == int(liczby[2]):
        print(liczby)