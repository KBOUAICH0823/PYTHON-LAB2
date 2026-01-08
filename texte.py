texte = input("دخل كلمة أو جملة: ")

print("الطول:", len(texte))
print("Majuscules:", texte.upper())
print("Minuscules:", texte.lower())
print("Inversion:", texte[::-1])

# Palindrome
texte_net = texte.replace(" ", "").lower()
if texte_net == texte_net[::-1]:
    print("هاد النص palindrome ✅")
else:
    print("هاد النص ماشي palindrome ❌")
