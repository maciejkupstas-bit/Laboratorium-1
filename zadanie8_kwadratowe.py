import math

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

if a == 0:
    print("Błąd: a musi być różne od 0")
else:
    delta = b ** 2-4 * a * c
    print(f"Delta = {delta}")

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Dwa pierwiastki: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x= -b/(2*a)
        print(f"jeden pierwiastek podwójny: x = {x}")
    else:
        print("Brak pierwiastków rzeczywistych")
