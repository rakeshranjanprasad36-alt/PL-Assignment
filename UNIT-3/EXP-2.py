# tempconv/__init__.py
from .c_to_f import to_fahrenheit
from .f_to_c import to_celsius
from .c_to_k import to_kelvin

# tempconv/c_to_f.py
def to_fahrenheit(c):
    return (c * 9/5) + 32

# tempconv/f_to_c.py
def to_celsius(f):
    return (f - 32) * 5/9

# tempconv/c_to_k.py
def to_kelvin(c):
    return c + 273.15

# main_app.py
from tempconv import to_fahrenheit, to_celsius, to_kelvin

def start():
    print("Temperature Converter")
    print("1. C → F")
    print("2. F → C")
    print("3. C → K")

    opt = input("Choose option: ")

    if opt == "1":
        c = float(input("Celsius: "))
        res = to_fahrenheit(c)
        print(f"{c:.2f}°C = {res:.2f}°F")

    elif opt == "2":
        f = float(input("Fahrenheit: "))
        res = to_celsius(f)
        print(f"{f:.2f}°F = {res:.2f}°C")

    elif opt == "3":
        c = float(input("Celsius: "))
        res = to_kelvin(c)
        print(f"{c:.2f}°C = {res:.2f}K")

    else:
        print("Invalid option.")

if __name__ == "__main__":
    start()
