def poprawnosc(limie, nazwisko):
    wynik = limie[0].upper() + "." + nazwisko.capitalize()
    return wynik

print(poprawnosc("jan", "kowalski"))