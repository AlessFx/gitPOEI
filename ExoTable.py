liste_animaux = ["lapin" , "chat" , "chien", "chiot", "dragon", "ornithorynque"]

print ("1. Affichage de l'ensemble")
print ("")
for animal in liste_animaux :
    print (animal)
print ("")
print ("2. Affichage inversé")
print ("")
liste_animaux.reverse()
for animal in liste_animaux:
    print (animal)
print ("")
print ("3. Affichage trié")
print ("")
liste_animaux.sort()
for animal in liste_animaux:
    print (animal)
print ("")
print ("4. Ajout de troll, suppression des animaux domestiques")
print ("")
liste_animaux.append ("troll")
for animal_del in (("lapin","chat","chien","chiot")):
    liste_animaux.remove (animal_del);
for animal in liste_animaux :
    print (animal)

print ("")
import random
tableau_jeu=[]
# Initialisation d'une liste de 10 éléments
for i in range (0,10) :tableau_jeu.append (random.randint (1,10))
guess = int (input ("Quel est le chriffre à chercher ? "))

long_tableau_jeu = len (tableau_jeu)
# Curseur de position dans le tableau
chiffre = 0
# On parcourt la liste tant que la valeur n'a pas été trouvée
# ET que l'on ne dépasse pas la taille du tableau
while ((chiffre < long_tableau_jeu) and (tableau_jeu [chiffre] != guess)):
    chiffre += 1
    if ( chiffre < long_tableau_jeu ):
        print ("Gagné")
        break
    else :
        print ("Perdu")

print ("")
tableau_jeu2 = []
for i in range (0,10):
    tableau_jeu2.append (random.randint (1,10))

# Tri du tableau
tableau_jeu2.sort ()
guess2 = int (input ("Quel est le nombre entre 1 et 10 recherché :"))
long_tableau_jeu2 = len (tableau_jeu2)
chiffre2 = 0


# Parcours de la liste tant que valeur non trouvée
while ((chiffre2 < long_tableau_jeu2 ) and ( tableau_jeu2 [chiffre2] < guess2)):
    chiffre2 += 1
if ( tableau_jeu2 [chiffre2] == guess2 ):
    print ("Gagné")
else:
    print ("Perdu")