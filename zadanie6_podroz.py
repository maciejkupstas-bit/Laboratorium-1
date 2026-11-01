dystans = float(input("Podaj dystans podróży w km: "))
spalanie =float(input("Podaj średnie spalanie w litrach na 100 km: "))
cena_paliwa = 6.5
zuzycie = dystans * spalanie / 100
koszt = zuzycie * cena_paliwa

print(f"Przewidywane zużcyie paliwa: {zuzycie:.2f} 1")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")
