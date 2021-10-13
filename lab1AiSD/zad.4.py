def poprawnosc(limie, nazwisko):
    wynik = limie[0].upper() + "." + nazwisko.capitalize()
    return wynik

def funkcjaWfunkcji(imie, nazwisko, funkcja):
    if funkcja == "zad" :
        funkcja1 = poprawnosc(imie, nazwisko)
        return funkcja1

print(funkcjaWfunkcji("jan","kowalski", "zad"))