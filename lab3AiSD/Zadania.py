from typing import List


def numbers(n: int) -> None:
    if n < 0:
        return
    print(n)
    numbers(n - 1)


# numbers(20)


def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(8))


def power(number: int, n: int) -> int:
    if number == 0:
        return 0
    if n == 0:
        return 1
    return number * power(number, n - 1)


# print(power(4, 3))
# print(power(10, 0))


def reverse(txt: str) -> str:
    if len(txt) == 1:
        return txt
    return reverse(txt[1:]) + txt[0]


# print(reverse("Ola"))
# print(reverse("Krokodyl"))


def factorial(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    return factorial(n - 1) * n


# print(factorial(5))
# print(factorial(3))


def prime(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0 and prime(i):
            return False
    return True


# print(prime(17))
# print(prime(15))


def n_sums(n: int) -> List[int]:
    start = 10 ** (n - 1)
    stop = 10 ** n
    lista = []
    for i in range(start, stop):
        sp = 0
        sn = 0
        org = i
        j = n
        while i > 0:
            if j % 2 == 0:
                sp += i % 10
                i = int(i / 10)
            else:
                sn += i % 10
                i = int(i / 10)
            j -= 1
        if sp == sn:
            lista.append(org)
    return lista

# print(n_sums(7))


def remove_duplicates(txt: str) -> str:
    if len(txt) == 0:
        return txt
    if len(txt) == 1:
        return txt
    if txt[0] == txt[1]:
        return txt[0] + remove_duplicates(txt[2:])
    else:
        return txt[0] + remove_duplicates(txt[1:])


# txt = "Ollamaakotta889"
# print(remove_duplicates(txt))

# brak 10 i 8



