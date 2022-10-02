class Acteur:

    def __init__(self, nom, prenom):
        self.nom = nom,
        self.prenom = prenom

    def __str__(self):
        return 'Acteur(nom =' + str(self.nom) + ' ,prenom =' + str(self.prenom) + ')'

    # GETTER AND SETTER
    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom
