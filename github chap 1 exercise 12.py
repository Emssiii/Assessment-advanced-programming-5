import math

def area_square():
    side = float(input("Enter side length of square: "))
    print("Area of square =", side * side)

def area_circle():
    radius = float(input("Enter radius of circle: "))
    print("Area of circle =", math.pi * radius * radius)

def area_triangle():
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    print("Area of triangle =", 0.5 * base * height)

print("1: Area of Square")
print("2: Area of Circle")
print("3: Area of Triangle")

choice = int(input("Choose an option: "))
if choice == 1:
    area_square()
elif choice == 2:
    area_circle()
elif choice == 3:
    area_triangle()
else:
    print("Invalid choice")
print()
