# Nous allons voir avec l'exemple ci-dessous comment créer une variable et faire des opérations sur celle-cit
# Rappel : les lignes de code avec le caractère "#" sont des commentaires

nomb_personnes_recette = 3   # nombre de personnes prévues par la recette
# nombre en grammes de farine pour faire la recette pour 3 personnes
grammes_farine_recette = 300

nomb_personnes_invitees = 6    # nombre de personnes invitées
# multip est le multiplicateur qui va permettre d'obtenir la valeur multiplicatrice
multip = nomb_personnes_invitees / nomb_personnes_recette
# on multiplie la variable grammes_farine_recette par multip
grammes_farine_recette = grammes_farine_recette * multip

print(grammes_farine_recette)
