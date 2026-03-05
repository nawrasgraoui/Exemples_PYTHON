class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Age: {self.age}")


class Salarie(Personne):
    def __init__(self, nom, age, salaire):
        Personne.__init__(self, nom, age)
        self.salaire = salaire

    def afficher_salaire(self):
        print(f"Salaire: {self.salaire}")


class Etudiant(Personne):
    def __init__(self, nom, age, notes):
        Personne.__init__(self, nom, age)
        self.notes = notes

    def calculer_moyenne(self):
        return sum(self.notes) / len(self.notes)


class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, age, salaire, notes):
        Salarie.__init__(self, nom, age, salaire)
        Etudiant.__init__(self, nom, age, notes)

    def afficher_infos_completes(self):
        print(f"Nom: {self.nom}")
        print(f"Age: {self.age}")
        print(f"Salaire: {self.salaire}")
        print(f"Moyenne: {self.calculer_moyenne()}")


# Création du doctorant
d = Doctorant("Nawras", 21, 10000, [14, 16, 15])

d.afficher_infos()
d.afficher_salaire()
print("Moyenne:", d.calculer_moyenne())
d.afficher_infos_completes()