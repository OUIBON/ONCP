import pygame

pygame.init()

# Définir les dimensions de l'écran
largeur, hauteur = 1920, 1080

# Créer la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Affichage des personnages au milieu")

# Charger les images des personnages
image_personnage1 = pygame.image.load("personnage1.png")
image_personnage2 = pygame.image.load("personnage2.png")
image_personnage3 = pygame.image.load("personnage3.png")

# Définir les positions des personnages au milieu de l'écran
personnage_pos = {
    1: (largeur // 2 - image_personnage1.get_width() // 2, hauteur // 2 - image_personnage1.get_height() // 2),
    2: (largeur // 2 - image_personnage2.get_width() // 2, hauteur // 2 - image_personnage2.get_height() // 2),
    3: (largeur // 2 - image_personnage3.get_width() // 2, hauteur // 2 - image_personnage3.get_height() // 2)
}

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Afficher les personnages au milieu de l'écran
    fenetre.fill((255, 255, 255))  # Remplir l'écran avec une couleur blanche (fond)
    fenetre.blit(image_personnage1, personnage_pos[1])
    fenetre.blit(image_personnage2, personnage_pos[2])
    fenetre.blit(image_personnage3, personnage_pos[3])
    pygame.display.flip()

pygame.quit()