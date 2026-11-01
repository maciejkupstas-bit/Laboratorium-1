import random

dystans = random.randint(1, 1000)
spalanie = float(input("Podaj średnie spalanie w litrach na 100 km: "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa za litr: "))

zuzycie = dystans * spalanie / 100
koszt = zuzycie * cena_paliwa

print(f"Losowy dystans: {dystans} km")
print(f"Przewidywane zużycie paliwa: {zuzycie:.2f} l")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")