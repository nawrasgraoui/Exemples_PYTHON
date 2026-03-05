class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    def presentation(self):
        return f"Je suis {self.nom}, {self.age} ans"


personne1 = Personne("nawras", 21, "nawras@email.com")
personne2 = Personne("graoui", 21, "graoui@email.com")
personne3 = Personne("sophie", 34, "sophie@email.com")

print (personne1.presentation())