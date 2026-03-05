
class Etudiant:
    def __init__(self):
        self.__cin = "XK220011"      # private
        self._cne = "M12121212"      # protégée

    def afficher_prive(self):
        return self.__cin

nawras= Etudiant()

print(nawras._Etudiant__cin)
print(nawras._cne)