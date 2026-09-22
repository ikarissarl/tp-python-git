try:
    nombre = int(input("Entrez un nombre entier : "))
    if nombre % 2 == 0:
        print(f"{nombre} est un nombre pair.")
    else:
        print(f"{nombre} est un nombre impair.")
except ValueError:
    print("Veuillez entrer un nombre entier valide.")