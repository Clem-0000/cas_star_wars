import personnage


class Gentil(personnage.Personnage):
    def __init__(self, nom, prenom, gentil):
        personnage.Personnage.__init__(nom, prenom),
        self.gentil_personnage = gentil
