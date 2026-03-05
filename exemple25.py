#identification de la classe Personne
class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
personne1 = Personne('Nawras', 21, 'nawras@email.com')

# LECTURE des attributs (notation pointée)
print(f"Nom: {personne1.nom}")      
print(f"Âge: {personne1.age}")      
print(f"Email: {personne1.email}")  

# MODIFICATION des attributs
personne1.nom = 'Nawras Graoui'                 # Changement du nom
personne1.age += 1                             # Incrémentation de l'âge
personne1.email = 'nawras.graoui@email.com'     # Nouvel email

# Vérification des changements
print(f"Nouveau nom: {personne1.nom}")  
print(f"Nouvel âge: {personne1.age}")   #22