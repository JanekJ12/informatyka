def horner(liczba,x):#liczba - string, x - system w którym jest liczba w = int(liczba[0])
    for i in range(1,len(liczba)):
        w = x + int(liczba[i])
        return w

ciagi = []
with open("ciagi.txt") as plik:
    for linia in plik:
        ciagi.append(linia.strip())
print(ciagi)
for i in range(len(ciagi)):
    if ciagi[i][:len(ciagi[i])//2] == ciagi[i][len(ciagi[i])//2]:
        print(ciagi[i])
licznik = 0
for i in range(len(ciagi)):
    if "11" not in ciagi[i]:
        licznik += 1
print(licznik)


liczby =[]
for i in range(len(ciagi)):
    liczby.append(horner(ciagi[i],2))
print(liczby)

sito = []
for i in range(363000):
    sito.append(1)
for i in range(2, 363000):
    if sito[i] == 1:
        for j in range(i+i, 363000,i):
            sito[j] = 0
perwsze = []
for i in range(2,363000):
    if sito[i] == 1:
        perwsze.append(i)
print(perwsze)

for i in range(len(liczby)):
    czynniki= []
    for j in range(len(perwsze)):
        liczba = liczby[i]
        while liczba % perwsze[j] == 0:
            czynniki.append(perwsze[j])
            liczba = liczba // perwsze[j]
            if len(czynniki) > 2:
                break
    if len(czynniki) == 2:
        print(liczby[i], czynniki)