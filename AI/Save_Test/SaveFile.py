chaine = "Je suis une chaine de caractère à sauvegardé *¨£*¨M"

rep = input("Nom du Fichier : ")

def sauvegarder(nom_fichier, chaine):
    with open(f"Save/{nom_fichier}.txt", 'w', encoding='UTF-8') as fichier:
        fichier.write(chaine)

sauvegarder(rep, chaine)


