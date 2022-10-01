# Aujoud'hui, nous allons voir comment ajouter des fonctions à Python
# Une fonction sert à diviser un problème en un sous problème plus simple
# Pour définir une fonction, il faut utiliser le mot-clé 'def' + nom de la fonction et 2 parenthèses
# Voyons ici comment afficher une table de multiplication

def multiplication(nombre):
    n = 0
    while n < 11:
        n = n + 1
        print(nombre*n)

# Pour utiliser le code de la fonction, il faut appeler celle-cit par son nom :


multiplication(2)
