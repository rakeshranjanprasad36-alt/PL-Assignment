# geometry.py
import math as m

def area_circle(r):
    return m.pi * (r ** 2)

def area_rectangle(l, w):
    return l * w

def area_triangle(b, h):
    return 0.5 * b * h




# app.py
import geometry as geo

def run():
    print("Select shape for area calculation:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    opt = input("Enter your option: ")

    if opt == "1":
        r = float(input("Radius: "))
        result = geo.area_circle(r)
        print(f"Area of circle: {result:.2f}")

    elif opt == "2":
        l = float(input("Length: "))
        w = float(input("Width: "))
        result = geo.area_rectangle(l, w)
        print(f"Area of rectangle: {result:.2f}")

    elif opt == "3":
        b = float(input("Base: "))
        h = float(input("Height: "))
        result = geo.area_triangle(b, h)
        print(f"Area of triangle: {result:.2f}")

    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    run()