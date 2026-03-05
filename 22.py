class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometre = 0  # Valeur par défaut


# Création d'un objet
ma_voiture = Voiture("Porsche", "911", 2023)

# Affichage des informations
print("Marque :", ma_voiture.marque)
print("Modèle :", ma_voiture.modele)
print("Année :", ma_voiture.annee)
print("Kilométrage :", ma_voiture.kilometre)