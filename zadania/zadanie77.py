with open("tekst.txt") as plik:
    tekst = plik.readline()
    print(tekst)
    lista_napisow = tekst.split()
    print(lista_napisow)
    licznik = 0
    for napis in lista_napisow:
        for i in range(len(napis) - 1):
            if napis[i] == napis[i + 1]:
                licznik += 1
                break
    print(licznik)
    slownik = {}
    for znak in tekst:
        if znak != " " and znak != "\n":
            if znak in slownik:
                slownik[znak] += 1
            else:
                slownik[znak] = 1
    print(slownik)
    suma = sum(slownik.values())
    for krotka in sorted(slownik.items(), key=lambda x: x[1], reverse=True):
        print(krotka[0], ':' , krotka[1], '(', round(100*krotka[1]/suma, 2), '%)')

samogloski = "AEIOUY"
maks = 0
for litera in lista_napisow:
    n = 0
    if litera not in samogloski:
        n += 1
        if n > maks:
            maks = n
    else:
        n = 0
print(maks)