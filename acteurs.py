class Acteur:

    def __init__(self, nom, prenom, acteur_personnage=None):
        if acteur_personnage is None:
            acteur_personnage = ()
        self.nom = nom
        self.prenom = prenom
        self.acteur_personnage = acteur_personnage

    def __str__(self):
        return 'Acteur(nom =' + str(self.nom) + ' ,prenom =' + str(self.prenom) + ')'

    def nombre_personage(self):
        print(type(self.acteur_personnage))
        return len(self.acteur_personnage)

    # GETTER AND SETTER
    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def get_acteur_personnage(self):
        return self.acteur_personnage

    def set_acteur_personnage(self, acteur_personnage):
        self.acteur_personnage = acteur_personnage
