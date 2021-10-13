suma_max = 101
suma_po = 0

for i in range(100):
    a = input("Podaj liczbe: ")
    a = int(a)
    suma_po = suma_po + a
    if(suma_po < suma_max):
        continue
    else:
        break

print("Koniec zabawy, suma > 100")




