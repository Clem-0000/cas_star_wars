class Film:

    def __init__(self, titre, annee_sortie, num_episode, cout, recette):
        self.titre = titre,
        self.annee_sortie = annee_sortie,
        self.num_episode = num_episode,
        self.cout = cout,
        self.recette = recette

    def __str__(self):
        return 'Film(titre =' + str(self.titre) + ' ,annee_sortie =' + str(self.annee_sortie) \
               + ' ,num_episode =' + str(self.num_episode) + ' ,cout =' + str(self.cout) \
               + ' ,recette =' + str(self.recette) + ')'

    # GETTER AND SETTER
    def get_titre(self):
        return self.titre

    def set_titre(self, titre):
        self.titre = titre

    def get_annee_sortie(self):
        return self.annee_sortie

    def set_annee_sortie(self, annee_sortie):
        self.annee_sortie = annee_sortie

    def get_num_episode(self):
        return self.num_episode

    def set_num_episode(self, num_episode):
        self.num_episode = num_episode

    def get_cout(self):
        return self.cout

    def set_cout(self, cout):
        self.cout = cout

    def get_recette(self):
        return self.recette

    def set_recette(self, recette):
        self.recette = recette
