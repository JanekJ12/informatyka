print("Zadanie 60")
liczby = []
licznik = 0
zm1 = 0
zm2 = 0
with open("C:\\Users\\koluc\\Documents\\GitHub\\INF2bT\\ZbiorCKE\\liczby.txt","r") as plik:
    for linia in plik:
        liczba = int(linia)
        if liczba < 1000:
            licznik += 1
            zm1 = zm2
            zm2 = liczba

        liczby.append(liczba)

print(licznik,zm1,zm2)
#60.2
for liczba in liczby:
    listaDzielnikow = []
    for i in range(1, int(liczba**0.5)):
        if liczba % i == 0:
            listaDzielnikow.append(i)
            listaDzielnikow.append(liczba//i)
    if liczba % liczba ** 0.5 == 0:
        listaDzielnikow.append(liczba**0.5)
    if len(listaDzielnikow) == 18:
        listaDzielnikow.sort()
        print(liczba,listaDzielnikow)
#60.3
najwieksza = 0

for liczba in liczby:
    względnie_pierwsza = True
    for inna in liczby:
        if liczba != inna:
            a, b = liczba, inna
            while b:
                a, b = b, a % b
            if a != 1:
                względnie_pierwsza = False
                break
    if względnie_pierwsza and liczba > najwieksza:
        najwieksza = liczba

print(f"{najwieksza}")