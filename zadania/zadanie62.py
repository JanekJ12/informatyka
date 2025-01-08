def horner(liczba,x):#liczba - string, x - system w którym jest liczba w = int(liczba[0])
    w = int(liczby8[0])
    for i in range(1,len(liczba)):
        w = x * w + int(liczba[i])
    return w

liczby8 = []
with open("C:\\Users\\koluc\\Documents\\GitHub\\INF2bT\\ZbiorCKE\\zadanie62\\liczby1.txt") as plik:
    for linia in plik:
        liczby8.append(linia.strip())
print(liczby8)
liczby10 = []
with open("C:\\Users\\koluc\\Documents\\GitHub\\INF2bT\\ZbiorCKE\\zadanie62\\liczby2.txt") as plik:
    for linia in plik:
        liczby10.append(linia.strip())
print(liczby10)

minimum = int(liczby8[0])
maks = int(liczby8[0])
for i in range (1,len(liczby8)):
    if minimum > int(liczby8[i]):
        minimum = int(liczby8[i])
    if maks < int(liczby8[i]):
        maks = int(liczby8[i])
print(minimum, maks)
pierwszy = int(liczby8[0])
pierwszyMaks = pierwszy
ilosc = 1
maksymalnaIlosc = 1
for i in range(len(liczby10)-1):
    if int(liczby10[i])<=int(liczby10[i+1]):
        ilosc += 1
        if ilosc > maksymalnaIlosc:
            maksymalnaIlosc = ilosc
            pierwszyMaks = pierwszy
    else:
        pierwszy = int(liczby10[i+1])
        ilosc = 1
print(maksymalnaIlosc, pierwszyMaks)

licznik = 0
licznik2 = 0
for i in range(len(liczby8)):
    if horner(liczby8[i], 8) == liczby10[i]:
        licznik += 1
    if horner(liczby8[i],8) > liczby10:
        licznik2 += 1
print(licznik, licznik2)