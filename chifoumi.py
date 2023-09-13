import random

manches = int(input("Jusqu'à combien de manches gagnantes voulez-vous jouer ? "))

score_joueur = 0
score_ordi = 0

options_ordi = ["pierre", "papier", "ciseaux"]
options_joueur = ["pierre", "papier", "ciseaux"]

while score_joueur < manches and score_ordi < manches:
    choix_joueur = input("Que jouez vous ? Tapez 'pierre', 'papier' ou 'ciseaux' ")

    choix_ordi = random.choice(options_ordi)

    if(choix_joueur not in options_joueur):
        print("Choix invalide !")
        choix_joueur = input("Que jouez vous ? Tapez 'pierre', 'papier' ou 'ciseaux' ")

    if(choix_ordi==choix_joueur):
        print("Egalité ! Veuillez rejouer !")

    elif choix_ordi == "pierre" and choix_joueur == "papier"\
    or choix_ordi == "papier" and choix_joueur == "ciseaux"\
    or choix_ordi == "ciseaux" and choix_joueur == "pierre":
        score_joueur = score_joueur+1
        print("Vous avez gagné ! Le score est de ", score_joueur,"à", score_ordi)
    else :
        score_ordi = score_ordi+1
        print("Vous avez perdu ! Le score est de ", score_joueur,"à", score_ordi)

if(manches == score_joueur):
    print("Partie gagné bien joué !")
elif(manches == score_ordi):
    print("Partie perdu dommage !")