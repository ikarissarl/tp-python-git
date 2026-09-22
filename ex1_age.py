nom = input("Quel est votre nom ? ")
annee_naissance = int(input("En quelle année êtes-vous né(e) ? "))
annee_actuelle = 2026
try:
    age = annee_actuelle - annee_naissance
    print(f"Bonjour {nom}, vous avez {age} ans.")
except ValueError:
    print("Veuillez entrer une année de naissance valide.")
