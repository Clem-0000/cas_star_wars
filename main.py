import acteurs
import film
import personnage

# création de 3 film
film1 = film.Film("Un nouvel espoir", 1977, 4, 11000000, 775400000)
film2 = film.Film("L'Empire contre attaque", 1980, 5, 11000000, 775400000)

titre = str(input("saisir le titre du film : "))
annee_sortie = int(input("saisir l'année de sortie du film : "))
num_episode = int(input("saisir le numéro d'épisode du film : "))
cout = int(input("saisir le coût du film : "))
recette = int(input("saisir la recette du film : "))

film3 = film.Film(titre, annee_sortie, num_episode, cout, recette)
print(film3)

# création d'un personnage
personnageFilm = personnage.Personnage("Anakin", "Skywalker")

# création collection
saga = [film1, film2, film3]
