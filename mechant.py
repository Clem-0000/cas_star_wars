import personnage


class Mechant(personnage.Personnage):
    def __init__(self, nom, prenom, gentil):
        super().__init__(nom, prenom)
        self.gentil = gentil
