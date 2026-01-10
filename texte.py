texte = input("Entrez un mot ou une phrase : ")

print("Longueur :", len(texte))
print("Majuscules :", texte.upper())
print("Minuscules :", texte.lower())
print("Inversion :", texte[::-1])

texte_net = texte.replace(" ", "").lower()
if texte_net == texte_net[::-1]:
    print("Ce texte est un palindrome ")
else:
    print("Ce texte n'est pas un palindrome ")

