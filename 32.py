class Personne:
    def __init__(self, nom, age):
        self.nom = nom      # passe par le setter si tu en ajoutes un
        self.age = age      # passe par @age.setter (validation)

    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("Entrez une valeur INT")
        if valeur < 0:
            raise ValueError("La valeur ne peut pas être moins que 0")
        if valeur > 140:
            raise ValueError("L'âge ici est irréaliste")
        self._age = valeur


# Tests / exemples
personne1 = Personne("Nawras", 21)
personne2 = Personne("Graoui", 21)
personne3 = Personne("Bad", 34)

print(personne1.age)
personne1.age = 30
print(personne1.age)

print(personne2.se_presenter())
print(personne3.se_presenter())