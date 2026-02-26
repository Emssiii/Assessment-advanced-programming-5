a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("It is a valid triangle.")
    # Optional extension: classify
    if a == b == c:
        print("It is an Equilateral triangle.\n")
    elif a == b or b == c or a == c:
        print("It is an Isosceles triangle.\n")
    else:
        print("It is a Scalene triangle.\n")
else:
    print("Not a valid triangle.\n")