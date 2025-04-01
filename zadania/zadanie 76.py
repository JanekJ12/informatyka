def szyfruj(napis, klucz):
    if not klucz:
        raise ValueError("Klucz szyfrujący jest pusty!")

    n = len(klucz)
    napis = list(napis)
    for i in range(len(napis)):
        j = klucz[i % n] - 1
        napis[i], napis[j] = napis[j], napis[i]
    return "".join(napis)

def deszyfruj(napis, klucz):
    if not klucz:
        raise ValueError("Klucz deszyfrujący jest pusty!")

    n = len(klucz)
    odwrotny_klucz = [0] * n
    for i, k in enumerate(klucz):
        odwrotny_klucz[k - 1] = i + 1
    napis = list(napis)
    for i in reversed(range(len(napis))):
        j = odwrotny_klucz[i % n] - 1
        napis[i], napis[j] = napis[j], napis[i]
    return "".join(napis)

# Zadanie 76.1
try:
    with open("szyfr1.txt", "r") as f:
        linie = f.read().splitlines()

    if len(linie) < 7:
        raise ValueError("Plik szyfr1.txt ma za mało wierszy!")

    napisy = linie[:6]
    klucz = list(map(int, linie[6].split()))

    wyniki = [szyfruj(napis, klucz) for napis in napisy]
    with open("wyniki_szyfr1.txt", "w") as f:
        f.write("\n".join(wyniki))
except Exception as e:
    print(f"Błąd w zadaniu 76.1: {e}")

# Zadanie 76.2
try:
    with open("szyfr2.txt", "r") as f:
        linie = f.read().splitlines()

    if len(linie) < 2:
        raise ValueError("Plik szyfr2.txt ma za mało wierszy!")

    napis = linie[0].strip()
    klucz = list(map(int, linie[1].split()))

    wynik = szyfruj(napis, klucz)
    with open("wyniki_szyfr2.txt", "w") as f:
        f.write(wynik)
except Exception as e:
    print(f"Błąd w zadaniu 76.2: {e}")

# Zadanie 76.3
try:
    with open("szyfr3.txt", "r") as f:
        linie = f.read().splitlines()

    if len(linie) < 2:
        raise ValueError("Plik szyfr3.txt ma za mało wierszy!")

    zaszyfrowany_napis = linie[0].strip()
    klucz = list(map(int, linie[1].split()))

    odszyfrowany_napis = deszyfruj(zaszyfrowany_napis, klucz)
    with open("wyniki_szyfr3.txt", "w") as f:
        f.write(odszyfrowany_napis)
except Exception as e:
    print(f"Błąd w zadaniu 76.3: {e}")
