# Primeira versão, sem armazenar os números já impressos, repetindo calculos.
def print_fibonacci(n:int) -> None:
    for i in range(1, n + 1):
        print(fibonacci(i), end=" ")


def fibonacci(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Segunda versão, com uma lista para armazenar os números já impressos, sem repetir calculos.
def print_fibonacci_(n:int, already_printed:list = []) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    fibonacci_n = print_fibonacci_(n - 1, already_printed) + print_fibonacci_(n - 2, already_printed)

    if fibonacci_n not in already_printed:
        if fibonacci_n == 1: #Print extra para o 1, que aparece duas vezes.
            print(fibonacci_n, end=" ")

        print(fibonacci_n, end=" ")
        already_printed.append(fibonacci_n)

    return print_fibonacci_(n - 1, already_printed) + print_fibonacci_(n - 2, already_printed)


print_fibonacci(6)
print()
print_fibonacci_(6)
