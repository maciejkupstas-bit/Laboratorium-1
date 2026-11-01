a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

if a != 0:
    x= -b / a
    print(f"Jedno rozwiązanie: x = {x}")
elif b == 0:
 print("Nieskończenie wiele rozwiązań")
else:
 print("Brak rozwiązań")
