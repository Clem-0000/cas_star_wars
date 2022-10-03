import acteurs
import personnage


class Film:

    def __init__(self, titre, annee_sortie, num_episode, cout, recette, acteur=None):
        """
        Constructeur permettant de créer un objet film
        :param self:
        :param titre: titre du film
        :param annee_sortie: année de sortie du film
        :param num_episode: numéro d'épisode du film si Saga
        :param cout: cout de production du film
        :param recette: recette rapporté par le film
        :param acteur: liste d'objet de type acteur
        :return:
        """
        if acteur is None:
            acteur = []
        self.titre = titre
        self.annee_sortie = annee_sortie
        self.num_episode = num_episode
        self.cout = cout
        self.recette = recette
        # attribut acteur Q7
        self.acteur_film = acteur

    def __str__(self):
        """
        Permet d'afficher les valeurs des attributs de la classe et leurs noms
        :return: le nom de la valeur et sa valeur
        """
        return 'Film(titre =' + str(self.titre) + ' ,annee_sortie =' + str(self.annee_sortie) \
               + ' ,num_episode =' + str(self.num_episode) + ' ,cout =' + str(self.cout) \
               + ' ,recette =' + str(self.recette) + ' ,acteur_film =' + str(self.acteur_film) + ')'

    def nb_acteur(self):
        """
        permet de calculer le nombre d'acteur dans un film
        :return: le nombre d'acteur jouant dans un film
        """
        return len(self.acteur_film)

    def nb_personnage(self):
        """
        permet de calculer le nombre de personnage présent dans un film
        :return: le nombre de personnage présent dans un film
        """
        nb_personnage = 0
        for acteur in self.acteur_film:
            for acteur2 in acteur:
                nb_personnage += acteur2.nombre_personage()
        return nb_personnage

    def calcul_benefice(self):
        """
        permet de calculer les bénéfices ou déficites d'un film
        :return: True ou False si le film à fait des bénéfices ou non et le nombre de bénéfices ou déficites du film
        """
        montant_benefice = 0
        beneficiaire = False
        if self.recette > self.cout:
            montant_benefice = self.recette - self.cout
            beneficiaire = True
        else:
            montant_benefice = self.cout - self.recette
        est_beneficiaire = (montant_benefice, beneficiaire)
        return est_beneficiaire

    def isBefore(self, annee):
        """
        permet de savoir si le film a été tourné avant ou après la date passée en paramètre
        :param annee: une année donnée par l'utilisateur
        :return: si l'année du film est avant ou après l'année passée en paramètre
        """
        if self.annee_sortie < annee:
            return True
        else:
            return False

    def tri_acteur(self):
        """
        trie les acteurs dans un ordre alphabétique
        :return: une collection d'acteur triée alphabétiquement
        """
        print(self.acteur_film)
        for i in self.acteur_film:
            print("e",type(i))
            print(i)



    # GETTER AND SETTER
    def get_titre(self):
        """
        permet d'avoir le titre d'un film
        :return: le titre d'un film
        """
        return self.titre

    def set_titre(self, titre):
        """
        permet de modifier le titre d'un film
        :param titre: contient le nouveau nom du film
        :return: /
        """
        self.titre = titre

    def get_annee_sortie(self):
        """
        permet de récupérer l'année de sortie du film
        :return: retourne l'année de sortie du film
        """
        return self.annee_sortie

    def set_annee_sortie(self, annee_sortie):
        """
        permet de modifier l'année de sortie du film
        :param annee_sortie: nouvelle date de sortie du film
        :return: /
        """
        self.annee_sortie = annee_sortie

    def get_num_episode(self):
        """
        permet de récupérer le numéro de l'épisode du film
        :return: le numéro de l'épisode du film
        """
        return self.num_episode

    def set_num_episode(self, num_episode):
        """
        permet de modifier le numéro de l'épisode d'un film
        :param num_episode: contient le nouveau numéro de l'épisode
        :return: /
        """
        self.num_episode = num_episode

    def get_cout(self):
        """
        permet de récupérer le cout d'un film
        :return: retourne le cout du film
        """
        return self.cout

    def set_cout(self, cout):
        """
        permet de modifier le cout du film
        :param cout: contient le nouveau cout du film
        :return: /
        """
        self.cout = cout

    def get_recette(self):
        """
        permet de récupérer le nombre de recette d'un film
        :return: le nombre de recette d'un film
        """
        return self.recette

    def set_recette(self, recette):
        """
        permet de modifier la recette d'un film
        :param recette: contient la nouvelle recette du film
        :return: /
        """
        self.recette = recette

    def get_acteur_film(self):
        """
        permet de récupérer la collection d'acteur ayant joué dans un film
        :return: la collection d'acteur ayant joué dans un film
        """
        return self.acteur_film

    def set_acteur_film(self, acteur):
        """
        permet de modifier la collection d'acteur ayant joué dans un film
        :param acteur: la nouvelle collection d'acteur
        :return: /
        """
        self.acteur_film.append(acteur)
