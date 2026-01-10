choix = input("Choisissez la conversion (1: Celsius → F/K, 2: Fahrenheit → C) : ")

try:
    if choix == "1":
        c = float(input("Entrez la température en Celsius : "))
        f = c * 9/5 + 32
        k = c + 273.15
        print(f"{c}°C = {f}°F = {k}K")

    elif choix == "2":
        f = float(input("Entrez la température en Fahrenheit : "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c}°C")

    else:
        print("Choix invalide")

except ValueError:
    print("Erreur : veuillez entrer une valeur numérique")

