ciagi = []
with open("ciagi — kopia.txt") as plik:
    for linia in plik:
        liczby = [int(liczba) for liczba in linia.split()]
        if len(liczby) > 1:
            ciagi.append(liczby)

def czy_pelny_szescian(liczba):
    if liczba < 0:
        return False
    pierwiastek = round(liczba ** (1/3))
    return pierwiastek ** 3 == liczba

licznik = 0
maks_roznica = 0

for ciag in ciagi:
    roznica = ciag[1] - ciag[0]
    for i in range(1, len(ciag)):
        if roznica != ciag[i] - ciag[i - 1]:
            break
    else:
        licznik += 1
        if roznica > maks_roznica:
            maks_roznica = roznica

print(f"Liczba ciągów arytmetycznych: {licznik}")
print(f"Największa różnica w ciągach arytmetycznych: {maks_roznica}")

wyniki = []

for ciag in ciagi:
    max_szescian = None
    for liczba in ciag:
        if czy_pelny_szescian(liczba):
            if max_szescian is None or liczba > max_szescian:
                max_szescian = liczba
    if max_szescian is not None:
        wyniki.append(max_szescian)

if wyniki:
    print("\nNajwiększe liczby będące sześcianami w kolejnych ciągach:")
    for wynik in wyniki:
        print(wynik)
else:
    print("\nW żadnym ciągu nie znaleziono liczby będącej pełnym sześcianem.")
