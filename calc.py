try:
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    op = input("Choisissez l'opération (+, -, *, /) : ")

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        if b == 0:
            print("Erreur : division par zéro impossible")
            exit()
        res = a / b
    else:
        print("Opération invalide")
        exit()

    print(f"{a} {op} {b} = {res}")

except ValueError:
    print("Erreur : veuillez entrer des nombres valides")
