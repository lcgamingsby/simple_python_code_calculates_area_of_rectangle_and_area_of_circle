import math

try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        raise ValueError("Radius cannot be below negative.")
    area = math.pi * (radius ** 2)
    print(f"area of the circle: {area:.2f}")
except ValueError as e:
    print(e)
