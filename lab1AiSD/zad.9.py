dzienTygodnia = {1: 'Poniedzialek', 2: 'Wtorek', 3: 'Sroda', 4: 'Czwartek', 5: 'Piatek',
                 6: 'Sobota', 7: 'Niedziela'}

def szukaj(a):
    for numer in dzienTygodnia:
        if (numer == a):
            return dzienTygodnia[numer]



print(szukaj(4))
print(szukaj(1))
print(szukaj(7))
print(szukaj(4))