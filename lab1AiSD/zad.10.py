def palindrom(napis):
    dlugosc = len(napis)
    for x in range(dlugosc-1):
        if napis[x] != napis[dlugosc-1-x]:
            return 0
    return 1

zdanie= 'Kamil'
zdanie2 = 'mam'

print(palindrom(zdanie))
print(palindrom(zdanie2))


