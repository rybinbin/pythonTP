#########################################################
#      Programme initiation python                      #
# Date : 31.03.2017										#
# Auteur : Marc-Edouard RYBINSKI                        #
#########################################################

import os
import math


#
qsff




#fonction pour retourner la couleur de la case
def type_case(nb):
    if nb == 0:
        couleur_case = "zero"
    else:
        test_paire = nb % 2
        if test_paire == 0:
            couleur_case = "red"
        else:
            couleur_case = "black"
    return couleur_case




# test de la fonction table
if __name__ == "__main__":
    table(4)
    os.system("pause")





# Fonction
# def table(nb, max=10):
#     """Fonction affichant la table de multiplication par nb de
#     1 * nb jusqu'à max * nb"""
#     i = 0
#     while i < max:
#         print(i + 1, "*", nb, "=", (i + 1) * nb)
#         i += 1

# # importer une seule fonction
# from math import sqrt
# #importer la libraire entièrerment
# import math
# d=math.sqrt(16)
# print(d)



# #lambda
# f=lambda x,y: x*y
# print(f(2,3))

# fonction lambda
# stupid = "Great again"
# chaine = "jsfpljds"

# def impr(chaine):
	# for i in chaine:
		# print(i)
	# return "Make"

# t=impr(stupid)
# print(t)

#boucle for
# essai="Je vous aime les loulous"
# for i in essai:
	# print(i)

# Boucle while

# test=0

# while test != 7:

	# test=input("Saisir une annee : ")
	# test=int(test)


#Test if
# test=input("Saisir une annee : ")
# test=int(test)

# if test < 1900 or test > 2017:
	# print("Are you Jesus ? ")
# else:
	# print("année saisie ok")
