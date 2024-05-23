import pygame
import time

# Initialisation de Pygame
pygame.init()

# Définition de la résolution de la fenêtre
largeur, hauteur = 1920, 1080
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu avec images")


# Chargement des images
journal_img = pygame.image.load("journal.png")
die_img = pygame.image.load("die.png")

# Durée en secondes pour l'affichage de chaque image
duree_affichage_journal = 5
duree_affichage_clignotement = 0.03  # Temps initial entre chaque clignotement (plus rapide)
nombre_clignotements = 3

# Fonction pour afficher une image pendant une durée donnée
def afficher_image(image, duree):
    fenetre.blit(image, (0, 0))
    pygame.display.flip()
    time.sleep(duree)

# Fonction pour faire clignoter une image un nombre de fois donné avec un intervalle entre chaque clignotement
def clignoter_image(image, nombre_clignotements, intervalle_clignotement):
    for _ in range(nombre_clignotements):
        fenetre.blit(image, (0, 0))
        pygame.display.flip()
        time.sleep(intervalle_clignotement)
        fenetre.fill((0, 0, 0))  # Efface l'écran en le remplissant de noir
        pygame.display.flip()
        time.sleep(intervalle_clignotement)

# Fonction pour alterner entre les deux images
def alterner_images():
    global duree_affichage_clignotement  # Déclarer la variable comme globale
    while True:
        afficher_image(journal_img, duree_affichage_journal)
        clignoter_image(die_img, nombre_clignotements, duree_affichage_clignotement)
        # Divise par deux la distance entre les apparitions de l'image "die.png"
        duree_affichage_clignotement /= 2

# Exécuter la fonction d'alternance des images
alterner_images()

# Quitter Pygame
pygame.quit()