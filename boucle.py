# Ce petit programme est un exemple de boucle
# Ici, nous allons afficher dans la console le nombre
# de caractères présents dans une chaîne de caractères que vous aurez entrée au préalable

# input est une fonction de python qui permet à l'utilisateur d'entrer des données au clavier.
chaine = input()
# L'exécution du programme s'arrêtera tant que vous n'avez pas appuyé sur la touche Entrée de votre clavier.
# Appuyer sur cette touche indique à Python de passer à la suite du programme.

n_car = 0         # nombre de caractères entrées

# len signifie "lenght" en python. Cela correspond à la longueur d'une chaîne de caractères.
while n_car < len(chaine):
    # le nombre de caractères augmente de 1 par rapport à la valeur initiale.
    n_car = n_car + 1
    # si la boucle a déjà été itérée au moins une fois, alors l'instruction n_car = n_car + 1
    print(n_car)
    # augmentera n_car de 1 par rapport à la valeur attribuée lors de la précédente itération.
