def classify_triangle(side_a:float, side_b:float, side_c:float) -> str:
    if not is_triangle(side_a, side_b, side_c):
        return "não formam um triangulo válido"

    elif is_equilateral(side_a, side_b, side_c):
        return "Equilátero"

    elif is_isosceles(side_a, side_b, side_c):
        return "Isósceles"

    elif is_scalene:
        return "Escaleno"


def is_triangle(side_a:float, side_b:float, side_c:float) -> bool:
    if side_a + side_b >= side_c and side_a + side_c >= side_b and side_b + side_c >= side_a:
        return True
    else:
        return False
    

def is_isosceles(side_a:float, side_b:float, side_c:float) -> bool:
    if side_a == side_b or side_b == side_c or side_a == side_c:
        return True
    else:
        return False


def is_equilateral(side_a:float, side_b:float, side_c:float) -> bool:
    if side_a == side_b and side_b == side_c:
        return True
    else:
        return False
    

def is_scalene(side_a:float, side_b:float, side_c:float) -> bool:
    if side_a != side_b and side_b != side_c and side_a != side_c:
        return True
    else:
        return False


print(classify_triangle(1, 2, 3))
print(classify_triangle(1, 1, 2))
print(classify_triangle(3, 3, 3))
print(classify_triangle(1, 2, 5))
