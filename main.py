import acteurs
import film
import personnage


def parcour_collection_obj(collection):
    """ Affiche la méthode str des objets présent dans la collection choisie en parametre.
    """
    for value in collection:
        print(value)


def make_back_up(dict_film):
    """
    fonction qui fait un truc
    :param dict_film: la clé étant le film et la valeur l'objet film
    :return: l'année le titre et le bénéfice
    """
    for objet_film in dict_film.items():
        return str(objet_film[0]) + " - " + str(objet_film[1].titre) + " - " + str(objet_film[1].calcul_benefice()[0])


# création de 3 film
film1 = film.Film("Un nouvel espoir", 1977, 4, 11000000, 775400000)
film2 = film.Film("L'Empire contre attaque", 1980, 5, 11000000, 775400000)

titre = str(input("saisir le titre du film : "))
annee_sortie = int(input("saisir l'année de sortie du film : "))
num_episode = int(input("saisir le numéro d'épisode du film : "))
cout = int(input("saisir le coût du film : "))
recette = int(input("saisir la recette du film : "))

film3 = film.Film(titre, annee_sortie, num_episode, cout, recette)

# création d'un personnage
personnageFilm = personnage.Personnage("Anakin", "Skywalker")

# création collection
saga = [film1, film2, film3]

# appel de la fonction parcour_collection_obj
parcour_collection_obj(saga)

# création d'un acteur incarnant deux personnages
personnage_joue1 = personnage.Personnage("Anakin", "Skywalker")
personnage_joue2 = personnage.Personnage("Dark", "Vador")
personnage_joue_harry = personnage.Personnage("Han", "Solo")
personnage_Natalie = personnage.Personnage("Reine", "Padme")
personnage_Ewan = personnage.Personnage("Obi-Wan", "Kenobi")

est_acteur = acteurs.Acteur("Hayden", "Christensen", (personnage_joue1, personnage_joue2))
est_acteur2 = acteurs.Acteur("Harrisson", "Ford", (personnage_joue_harry,))
est_acteur3 = acteurs.Acteur("Portman", "Natalie", (personnage_Natalie,))
est_acteur4 = acteurs.Acteur("Mcgregor", "Ewan", (personnage_Ewan,))

# création d'une collection d'acteurs
saga_acteurs = [est_acteur, est_acteur2, est_acteur3, est_acteur4]

# retourne le nombre de personnages incarnés par l'acteur
print(
    f"fonction nb_personnage class Acteur : nombre personnage incarnés par l'acteur {est_acteur.nom} {est_acteur.prenom} : {est_acteur.nombre_personage()} ")

# test de la fonction de calcul du nombre d'acteurs
saga[2].set_acteur_film(saga_acteurs)
print("fonction nb_acteur : nombre acteur", saga[2].nb_acteur())

# test de la fonction de calcul du nombre de personnages
print("fonction nb_personnage class Film : nombre personnage : ", saga[2].nb_personnage())

# test de la fonction de calcul des bénéfices
print("fonction bénéfice: bénéfice? : ", saga[2].calcul_benefice())

# test de la fonction isBefore()
year = int(input("saisir une année : "))
print("fonction isBefore : est sortie avant votre année proposé : ", saga[2].isBefore(year))

# test de la fonction tri
listeNomActeurTrie = []
for i in saga[2].acteur_film:
    listeNomActeurTrie.append(i.nom)
print("liste des acteurs avant le trie : ", listeNomActeurTrie)

saga[2].tri_acteur()

listeNomActeurTrie = []
for i in saga[2].acteur_film:
    listeNomActeurTrie.append(i.nom)
print("liste des acteurs après le trie : ", listeNomActeurTrie)

# test de la fonction mackBackUp
print("question 13 : ", make_back_up({1977: film1}))
