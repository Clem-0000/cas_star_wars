class Personnage:

    def __init__(self, nom_perso, prenom_perso):
        self.nom_perso = nom_perso,
        self.prenom_perso = prenom_perso

    def __str__(self):
        return 'Acteur(nom_perso =' + str(self.nom_perso) + ' ,prenom_perso =' + str(self.prenom_perso) + ')'

    # GETTER AND SETTER
    def get_nom_perso(self):
        return self.nom_perso

    def set_nom_perso(self, nom):
        self.nom_perso = nom

    def get_prenom_perso(self):
        return self.prenom_perso

    def set_prenom_perso(self, prenom):
        self.prenom_perso = prenom
