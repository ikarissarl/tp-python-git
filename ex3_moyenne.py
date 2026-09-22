def calculer_moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)
mes_notes = [14, 16, 12, 18, 10]
moyenne = calculer_moyenne(mes_notes)
print(f"La moyenne des notes est : {moyenne}")
    