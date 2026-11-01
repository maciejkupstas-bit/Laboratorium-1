a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print(f"Suma: {a + b}")
print(f"Różnica: {a - b}")
print(f"Iloczyn: {a * b}")

if b != 0:
    print(f"Iloraz: {a / b}")
else:
    print("Nie można dzielić przez zero")

print(f"Potęgowanie: {a ** b}")