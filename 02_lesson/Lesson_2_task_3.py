import math

def square(side: float) -> int:
    return math.ceil(side * side)

side = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side)}")