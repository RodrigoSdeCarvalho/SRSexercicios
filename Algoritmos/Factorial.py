def recursive_factorial(n:int) -> int:
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


def iterative_factorial(n:int) -> int:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial


print(recursive_factorial(6))
print(iterative_factorial(6))
