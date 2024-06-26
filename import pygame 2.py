import pygame
import random
import sys
import time

pygame.init()

# Couleur bleue pour le texte de la batterie
couleur_bleue = (0, 0, 255)

# Définir les dimensions de l'écran
largeur, hauteur = 1920, 1080

# Créer la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("One Night at Cute Park")

# Chargement des images
image_bg_menu = pygame.image.load("imagebgmenu.png").convert_alpha()
image_start = pygame.image.load("start.png").convert_alpha()
image_quit = pygame.image.load("quit.png").convert_alpha()

# Positionnement des boutons
pos_start = (1000, 300)
pos_quit = (1000, 800)

# Fonction pour afficher le menu
def afficher_menu():
    fenetre.blit(image_bg_menu, (0, 0))
    fenetre.blit(image_start, pos_start)
    fenetre.blit(image_quit, pos_quit)
    pygame.display.flip()

# Boucle principale du jeu
running = True
afficher_menu()  # Afficher le menu au début

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if image_start.get_rect(topleft=pos_start).collidepoint(event.pos):
                print("Démarrage du jeu...")
                # Ici vous pouvez mettre le code pour démarrer votre jeu
                running = False
            elif image_quit.get_rect(topleft=pos_quit).collidepoint(event.pos):
                print("Quitter le jeu...")
                running = False
                break  # Sortir de la boucle principale uniquement lorsque le bouton "Quit" est cliqué

# Charger les images des nouveaux boutons bleus et rouges pour chaque porte
image_bouton_bleu_porte1 = pygame.image.load("bp1.png")
image_bouton_rouge_porte1 = pygame.image.load("br1.png")
image_bouton_bleu_porte2 = pygame.image.load("bp2.png")
image_bouton_rouge_porte2 = pygame.image.load("br2.png")

# Position des nouveaux boutons pour chaque porte
pos_bouton_bleu_gauche = (100, 500)
pos_bouton_rouge_gauche = (200, 500)
pos_bouton_bleu_droite = (1300, 500)
pos_bouton_rouge_droite = (1400, 500)

# Initialiser l'état de chaque porte
porte1_ouverte = False
porte2_ouverte = False

# Charger les images
image_background = pygame.image.load("background.png")
image_porte_lumiere = pygame.image.load("image_porte_lumiere.png")
image_porte_fermee = pygame.image.load("image_porte_fermee.png")
image_personnage1 = pygame.image.load("personnage1.png")
image_personnage2 = pygame.image.load("personnage2.png")
image_personnage3 = pygame.image.load("personnage3.png")

image_imagedefin = pygame.image.load("imagedefin.png")
image_perdu = pygame.image.load("imageperdu.png")
image_porte_normale = pygame.image.load("image_porte_normale.png")  # Ajout de l'image normale de la porte

# Charger les images des caméras
images_cameras = {
    1: pygame.image.load("imagebg1.png"),
    2: pygame.image.load("imagebg2.png"),
    3: pygame.image.load("imagebg3.png"),
    4: pygame.image.load("imagebg4.png"),
    5: pygame.image.load("imagebg5.png"),
}

camera_active = None  # ou une valeur initiale appropriée

if camera_active is not None:
    image_fond_active = images_cameras[camera_active]
else:
    image_fond_active = None

etats_cameras = {1: False, 2: False, 3: False, 4: False, 5: False}
camera_active = None  # ou une valeur initiale appropriée

# toogle la cam
def toggle_camera(numero_camera):
    global etats_cameras, camera_active

    # Basculez l'état de la caméra
    etats_cameras[numero_camera] = not etats_cameras[numero_camera]

    # Si la caméra est maintenant ouverte, activez-la
    if etats_cameras[numero_camera]:
        camera_active = numero_camera
    else:
        # Si la caméra est maintenant fermée, désactivez-la
        camera_active = None

    update_personnages_visibles()  # Ajoutez cette fonction si elle n'est pas déjà présente

# Charger les images des boutons
image_bouton_1 = pygame.image.load("1.png")
image_bouton_2 = pygame.image.load("2.png")
image_bouton_3 = pygame.image.load("3.png")
image_bouton_4 = pygame.image.load("4.png")
image_bouton_5 = pygame.image.load("5.png")

# Charger les images des boutons actifs une seule fois
image_bouton_active_1 = pygame.image.load("imagebg1.png")
image_bouton_active_2 = pygame.image.load("imagebg2.png")
image_bouton_active_3 = pygame.image.load("imagebg3.png")
image_bouton_active_4 = pygame.image.load("imagebg4.png")
image_bouton_active_5 = pygame.image.load("imagebg5.png")

# Définir les positions initiales des personnages relativement au haut de l'écran (pour un écran 1920 x 1080)
scale_factor_x = 1920 / 304
scale_factor_y = 1080 / 580

personnage_pos = {
    1: (1920 // 2, int(1080 // 4)),  # en haut au milieu
    2: (int(1920 // 4), int(1080 // 4)),  # en haut à gauche
    3: (int(3 * 1920 // 4), int(1080 // 4))  # en haut à droite
}

# Position des nouveaux boutons pour chaque porte
pos_bouton_bleu_porte1 = (100, 500)
pos_bouton_rouge_porte1 = (200, 500)
pos_bouton_bleu_porte2 = (1300, 500)
pos_bouton_rouge_porte2 = (1400, 500)

# Définir les positions initiales
bouton1_pos = (1600, 650)
bouton2_pos = (1750, 750)
bouton3_pos = (1450, 750)
bouton4_pos = (1450, 850)
bouton5_pos = (1750, 850)  # Déplacer les boutons vers le bas

# Définir les positions initiales des caméras
positions_cameras = {
    1: [bouton1_pos],
    2: [bouton2_pos],
    3: [bouton3_pos],
    4: [bouton4_pos],
    5: [bouton5_pos]
}

# Définir les positions initiales
background_pos = (0, 0)
porte1_pos = (100, 200)
porte2_pos = (1500, 200)

# Afficher les images des boutons
fenetre.blit(image_bouton_1, (bouton1_pos[0] - 20, bouton1_pos[1] - 20))
fenetre.blit(image_bouton_2, (bouton2_pos[0] - 20, bouton2_pos[1] - 20))
fenetre.blit(image_bouton_3, (bouton3_pos[0] - 20, bouton3_pos[1] - 20))
fenetre.blit(image_bouton_4, (bouton4_pos[0] - 20, bouton4_pos[1] - 20))
fenetre.blit(image_bouton_5, (bouton5_pos[0] - 20, bouton5_pos[1] - 20))

# Définir la largeur et la hauteur des boutons
largeur_bouton = 100
hauteur_bouton = 50

# Créer les rectangles pour les collisions
background_rect = pygame.Rect(background_pos, (largeur, hauteur))
porte1_rect = pygame.Rect(porte1_pos, (image_porte_lumiere.get_width(), image_porte_lumiere.get_height()))
porte2_rect = pygame.Rect(porte2_pos, (image_porte_lumiere.get_width(), image_porte_lumiere.get_height()))

# Nouveaux rectangles pour les collisions avec les nouveaux boutons associés à chaque porte
bouton_bleu_rect_gauche = pygame.Rect(pos_bouton_bleu_gauche, (largeur_bouton, hauteur_bouton))
bouton_rouge_rect_gauche = pygame.Rect(pos_bouton_rouge_gauche, (largeur_bouton, hauteur_bouton))
bouton_bleu_rect_droite = pygame.Rect(pos_bouton_bleu_droite, (largeur_bouton, hauteur_bouton))
bouton_rouge_rect_droite = pygame.Rect(pos_bouton_rouge_droite, (largeur_bouton, hauteur_bouton))

bouton1_rect = pygame.Rect(bouton1_pos, (image_bouton_bleu_porte2.get_width(), image_bouton_bleu_porte2.get_height()))
bouton2_rect = pygame.Rect(bouton2_pos, (image_bouton_bleu_porte2.get_width(), image_bouton_bleu_porte2.get_height()))
bouton3_rect = pygame.Rect(bouton3_pos, (image_bouton_bleu_porte2.get_width(), image_bouton_bleu_porte2.get_height()))
bouton4_rect = pygame.Rect(bouton4_pos, (image_bouton_bleu_porte2.get_width(), image_bouton_bleu_porte2.get_height()))
bouton5_rect = pygame.Rect(bouton5_pos, (image_bouton_bleu_porte2.get_width(), image_bouton_bleu_porte2.get_height()))

# Initialiser les états
bouton_bleu_appuye = False
bouton_rouge_appuye = False

# Initialiser le temps imparti
temps_debut = pygame.time.get_ticks()
temps_fin = temps_debut + 9 * 45 * 1000  # 8 minutes en millisecondes

# Initialiser la batterie
pourcentage_batterie = 100
temps_derniere_maj_batterie = pygame.time.get_ticks()

# Charger la police d'écriture
font_batterie = pygame.font.Font(None, 36)

# Définir la couleur du texte de la batterie
couleur_texte_batterie = (255, 255, 255)

# Position du texte de la batterie
position_texte_batterie = (10, 10)

# Définir la variable temps_dernier_deplacement
temps_dernier_deplacement = pygame.time.get_ticks()

# Initialiser les états des images
image_porte_lumiere_active = False
image_porte_fermee_active = False
camera_active = None

# Initialiser les positions initiales des personnages
personnage_pos = {1: bouton1_pos, 2: bouton1_pos, 3: bouton1_pos}

positions_initiales_des_personnages = {
    1: (1920 // 2, int(1080 // 4)),  # en haut au milieu
    2: (int(1920 // 4), int(1080 // 4)),  # en haut à gauche
    3: (int(3 * 1920 // 4), int(1080 // 4))  # en haut à droite
}

# Initialiser l'état du dernier bouton appuyé
dernier_bouton_appuye = None

# Initialiser le numéro de la caméra active
camera_active = None

# Initialiser les personnages visibles pour chaque caméra
personnages_visibles = {1: set(), 2: set(), 3: set(), 4: set(), 5: set()}

# Initialiser le temps
temps_debut = pygame.time.get_ticks()
temps_precedent = temps_debut

# Textes à afficher
font_heure = pygame.font.Font(None, 36)
textes = ["23h", "00h", "01h", "02h", "03h", "04h", "05h", "06h", "07h", "08h"]
indice_texte = 0

#couleur fond
couleur_fond = (0, 0, 0)  # Remplacez cela par la couleur de fond réelle de votre jeu

# Créer une surface de masquage avec la couleur du fond
masquage = pygame.Surface((largeur, hauteur))
masquage.fill(couleur_fond)

# Définition de la fonction update_personnages_visibles
def update_personnages_visibles():
    global camera_active, image_porte_lumiere_active, personnages_visibles

    # Réinitialiser les personnages visibles pour la caméra active
    if camera_active is not None:
        personnages_visibles[camera_active] = set()

        for personnage, pos in personnage_pos.items():
            if pos == porte1_pos or pos == porte2_pos:
                if image_porte_lumiere_active:
                    personnages_visibles[camera_active].add(personnage)
            elif pos in positions_cameras[camera_active]:
                personnages_visibles[camera_active].add(personnage)

if camera_active is not None:
    image_fond_active = globals()[f"image_bg{camera_active}"]
else:
    image_fond_active = None

# Définir les dimensions de l'image imagedefin
largeur_image_imagedefin = image_imagedefin.get_width()
hauteur_image_imagedefin = image_imagedefin.get_height()

# Définir la position pour l'image "image_imagedefin" au centre de l'écran
imagedefin_pos = ((1920 - largeur_image_imagedefin) // 2, (1080 - hauteur_image_imagedefin) // 2)

# Définir la position pour l'image "imageperdu" au centre de l'écran
perdu_pos = ((largeur - 1920) // 2, (hauteur - 1080) // 2)

positions_cameras = {
    1: [bouton1_pos],
    2: [bouton2_pos],
    3: [bouton3_pos],
    4: [bouton4_pos],
    5: [bouton5_pos]
}

temps_porte_fermee = 0


# Initialiser mouse_x et mouse_y en dehors de la boucle principale
mouse_x, mouse_y = 0, 0


# Définition des rectangles des boutons pour les portes 1 et 2
bouton_bleu_porte1_rect = image_bouton_bleu_porte1.get_rect()
bouton_bleu_porte1_rect.x = pos_bouton_bleu_porte1[0]
bouton_bleu_porte1_rect.y = pos_bouton_bleu_porte1[1]

bouton_rouge_porte1_rect = image_bouton_rouge_porte1.get_rect()
bouton_rouge_porte1_rect.x = pos_bouton_rouge_porte1[0]
bouton_rouge_porte1_rect.y = pos_bouton_rouge_porte1[1]

bouton_bleu_porte2_rect = image_bouton_bleu_porte2.get_rect()
bouton_bleu_porte2_rect.x = pos_bouton_bleu_porte2[0]
bouton_bleu_porte2_rect.y = pos_bouton_bleu_porte2[1]

bouton_rouge_porte2_rect = image_bouton_rouge_porte2.get_rect()
bouton_rouge_porte2_rect.x = pos_bouton_rouge_porte2[0]
bouton_rouge_porte2_rect.y = pos_bouton_rouge_porte2[1]

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Mettre à jour la position de la souris

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Gérer les événements des nouveaux boutons
            if bouton_bleu_porte1_rect.collidepoint(mouse_x, mouse_y):
                porte1_ouverte = not porte1_ouverte
            elif bouton_rouge_porte1_rect.collidepoint(mouse_x, mouse_y):
                porte1_ouverte = not porte1_ouverte
            elif bouton_bleu_porte2_rect.collidepoint(mouse_x, mouse_y):
                porte2_ouverte = not porte2_ouverte
            elif bouton_rouge_porte2_rect.collidepoint(mouse_x, mouse_y):
                porte2_ouverte = not porte2_ouverte

    # Mise à jour des positions des boutons si nécessaire
    bouton_bleu_porte1_rect.x = pos_bouton_bleu_porte1[0]
    bouton_bleu_porte1_rect.y = pos_bouton_bleu_porte1[1]

    bouton_rouge_porte1_rect.x = pos_bouton_rouge_porte1[0]
    bouton_rouge_porte1_rect.y = pos_bouton_rouge_porte1[1]

    bouton_bleu_porte2_rect.x = pos_bouton_bleu_porte2[0]
    bouton_bleu_porte2_rect.y = pos_bouton_bleu_porte2[1]

    bouton_rouge_porte2_rect.x = pos_bouton_rouge_porte2[0]
    bouton_rouge_porte2_rect.y = pos_bouton_rouge_porte2[1]

    # Gérer les interactions des portes
    if porte1_ouverte:
        # Afficher l'image de la porte ouverte pour la porte 1
        fenetre.blit(image_porte_lumiere, porte1_pos)
    else:
        # Afficher l'image de la porte fermée pour la porte 1
        fenetre.blit(image_porte_fermee, porte1_pos)

    if porte2_ouverte:
        # Afficher l'image de la porte ouverte pour la porte 2
        fenetre.blit(image_porte_lumiere, porte2_pos)
    else:
        # Afficher l'image de la porte fermée pour la porte 2
        fenetre.blit(image_porte_fermee, porte2_pos)

    # Gérer les interactions des boutons existants
    if bouton1_rect.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton 1 est cliqué
        pass
    elif bouton2_rect.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton 2 est cliqué
        pass
    elif bouton3_rect.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton 3 est cliqué
        pass
    
    # Gérer les interactions des nouveaux boutons associés à chaque porte
    elif bouton_bleu_rect_gauche.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton bleu de gauche est cliqué
        pass
    elif bouton_rouge_rect_gauche.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton rouge de gauche est cliqué
        pass
    elif bouton_bleu_rect_droite.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton bleu de droite est cliqué
        pass
    elif bouton_rouge_rect_droite.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton rouge de droite est cliqué
        pass

    update_personnages_visibles()  # Assurez-vous d'appeler cette fonction ici s'il n'est pas déjà appelé dans votre code

    # Déplacer les personnages toutes les 15 secondes
    temps_actuel_millis = pygame.time.get_ticks()
    temps_ecoule_deplacement = temps_actuel_millis - temps_dernier_deplacement

    if temps_ecoule_deplacement >= 15000:  # 15 secondes
        temps_dernier_deplacement = temps_actuel_millis

        for personnage in personnage_pos:
            available_positions = []

            # Définir les positions disponibles en fonction des règles du jeu
            if personnage_pos[personnage] == bouton1_pos:
                available_positions = [bouton2_pos, bouton3_pos]
            elif personnage_pos[personnage] == bouton2_pos:
                available_positions = [bouton1_pos, bouton3_pos, bouton4_pos]
            elif personnage_pos[personnage] == bouton3_pos:
                available_positions = [bouton1_pos, bouton2_pos, bouton5_pos]
            elif personnage_pos[personnage] == bouton4_pos:
                available_positions = [bouton2_pos, porte1_pos]
            elif personnage_pos[personnage] == bouton5_pos:
                available_positions = [bouton3_pos, porte2_pos]
            elif personnage_pos[personnage] == porte2_pos:
                available_positions = [bouton5_pos]
            elif personnage_pos[personnage] == porte1_pos:
                available_positions = [bouton4_pos]

            if available_positions:
                new_pos = random.choice(available_positions)
                personnage_pos[personnage] = new_pos

    # Gérer les interactions des portes
    if bouton_bleu_appuye:
        porte1_ouverte = True
        porte2_ouverte = True

    update_personnages_visibles()

    # Mettre à jour le temps
    temps_actuel_millis = pygame.time.get_ticks()

    if temps_actuel_millis - temps_debut >= temps_fin:
        fenetre.blit(image_imagedefin, imagedefin_pos)
        pygame.display.flip()
        pygame.time.wait(3000)  # Attente de 3 secondes avant de quitter
        pygame.quit()
        sys.exit()

    # Définir le facteur de consommation de base
    facteur_consommation_base = 1

    # Facteur de temps pour ajuster la vitesse de décharge
    facteur_temps_decharge = 0.01  # Modifiez cette valeur pour ajuster la vitesse de décharge

    # Mettre à jour la batterie en fonction du temps écoulé
    temps_ecoule_batterie = temps_actuel_millis - temps_derniere_maj_batterie

    # Fréquence de mise à jour de la batterie (en millisecondes)
    frequence_maj_batterie = 100  # Par exemple, mettez 100 pour une mise à jour toutes les 100 millisecondes

    # Mettre à jour la batterie plus fréquemment
    while temps_ecoule_batterie >= frequence_maj_batterie:
        temps_ecoule_batterie -= frequence_maj_batterie

        if pourcentage_batterie > 0:  # Vérifier si la batterie n'est pas déjà à 0%
            facteur_decharge_base = facteur_consommation_base * facteur_temps_decharge

            # Ajuster la décharge en fonction des actions spécifiques
            if image_porte_lumiere_active:
                facteur_decharge = 3 * facteur_temps_decharge  # La batterie se décharge plus rapidement avec les lumières
            elif camera_active is not None:
                facteur_decharge = 5 * facteur_temps_decharge  # La batterie se décharge plus rapidement avec les caméras
            elif not porte1_ouverte and not porte2_ouverte:
                facteur_decharge = 3 * facteur_temps_decharge  # La batterie se décharge plus rapidement lorsque les portes sont fermées
            else:
                facteur_decharge = facteur_decharge_base

            pourcentage_batterie -= facteur_decharge

            temps_derniere_maj_batterie = temps_actuel_millis

    # Afficher le pourcentage de batterie en temps réel
    texte_batterie = font_batterie.render(f"Batterie: {pourcentage_batterie:.2f}%", True, couleur_texte_batterie)
    fenetre.blit(texte_batterie, position_texte_batterie)

    # Fin du jeu si la batterie est à 0%
    if pourcentage_batterie <= 0:
        fenetre.blit(image_perdu, perdu_pos)  # Remplacez perdu_pos par la position de votre image "imageperdu"
        pygame.display.flip()
        pygame.time.wait(3000)  # Attente de 3 secondes avant de quitter
        pygame.quit()
        sys.exit()

    # Condition pour afficher une image de fond active
    if camera_active is not None:
        image_fond_active = images_cameras[camera_active]
    else:
        image_fond_active = None

    # Afficher l'image de fond
    fenetre.blit(image_background, background_pos)

    # Condition pour afficher une image de fond active
    if image_fond_active is not None:
        fenetre.blit(image_fond_active, background_pos)

    # Afficher les personnages
    fenetre.blit(image_personnage1, (personnage_pos[1][0] - 2000, personnage_pos[1][1] - 2000))
    fenetre.blit(image_personnage2, (personnage_pos[2][0] - 2000, personnage_pos[2][1] - 2000))
    fenetre.blit(image_personnage3, (personnage_pos[3][0] - 2000, personnage_pos[3][1] - 2000))

    # Afficher les portes et les boutons
    if image_porte_lumiere_active:
        fenetre.blit(image_porte_lumiere, porte1_pos)  # Afficher l'image lumière de la porte
        fenetre.blit(image_porte_lumiere, porte2_pos)  # Afficher l'image lumière de la porte
    elif image_porte_fermee_active:
        fenetre.blit(image_porte_fermee, porte1_pos)  # Afficher l'image fermée de la porte
        fenetre.blit(image_porte_fermee, porte2_pos)  # Afficher l'image fermée de la porte
    else:
        fenetre.blit(image_porte_normale, porte1_pos)  # Afficher l'image normale de la porte
        fenetre.blit(image_porte_normale, porte2_pos)  # Afficher l'image normale de la porte

    # Afficher les boutons
    fenetre.blit(image_bouton_bleu_porte1, pos_bouton_bleu_gauche)
    fenetre.blit(image_bouton_rouge_porte1, pos_bouton_rouge_gauche)
    fenetre.blit(image_bouton_bleu_porte2, pos_bouton_bleu_droite)
    fenetre.blit(image_bouton_rouge_porte2, pos_bouton_rouge_droite)

    # Afficher les images "imagebg(numéro).png" en utilisant les coordonnées (0, 0)
    if camera_active is not None:
        image_bg = images_cameras[camera_active]
        fenetre.blit(image_bg, (50, 50))

    # Afficher les boutons
    fenetre.blit(image_bouton_1, (bouton1_pos[0] - 20, bouton1_pos[1] - 20))
    fenetre.blit(image_bouton_2, (bouton2_pos[0] - 20, bouton2_pos[1] - 20))
    fenetre.blit(image_bouton_3, (bouton3_pos[0] - 20, bouton3_pos[1] - 20))
    fenetre.blit(image_bouton_4, (bouton4_pos[0] - 20, bouton4_pos[1] - 20))
    fenetre.blit(image_bouton_5, (bouton5_pos[0] - 20, bouton5_pos[1] - 20))

    # Afficher le pourcentage de batterie
    texte_batterie = font_batterie.render(f"Batterie: {pourcentage_batterie:.2f}%", True, couleur_texte_batterie)
    fenetre.blit(texte_batterie, position_texte_batterie)

    # Afficher le texte d'heure
    temps_actuel = pygame.time.get_ticks()
    temps_ecoule = temps_actuel - temps_precedent

    if temps_ecoule >= 45000:  # 45 secondes en millisecondes
        temps_precedent = temps_actuel
        indice_texte = (indice_texte + 1) % len(textes)  # Passer au texte suivant

    texte_heure = font_heure.render(f"Heure: {textes[indice_texte]}", True, couleur_bleue)
    fenetre.blit(texte_heure, (largeur - texte_heure.get_width() - 10, 10))

        # À ajouter après la boucle principale pour gérer les événements pygame.MOUSEBUTTONDOWN

    # Gérer les interactions des boutons associés à chaque porte
    if bouton_bleu_rect_gauche.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton bleu de gauche est cliqué pour la porte 1
        porte1_ouverte = not porte1_ouverte
    elif bouton_rouge_rect_gauche.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton rouge de gauche est cliqué pour la porte 1
        porte1_ouverte = not porte1_ouverte
    elif bouton_bleu_rect_droite.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton bleu de droite est cliqué pour la porte 2
        porte2_ouverte = not porte2_ouverte
    elif bouton_rouge_rect_droite.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton rouge de droite est cliqué pour la porte 2
        porte2_ouverte = not porte2_ouverte

    # Gérer les interactions des boutons associés à chaque caméra
    elif bouton1_rect.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton de la caméra 1 est cliqué
        toggle_camera(1)
    elif bouton2_rect.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton de la caméra 2 est cliqué
        toggle_camera(2)
    elif bouton3_rect.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton de la caméra 3 est cliqué
        toggle_camera(3)
    elif bouton4_rect.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton de la caméra 4 est cliqué
        toggle_camera(4)
    elif bouton5_rect.collidepoint(mouse_x, mouse_y):
        # Action lorsque le bouton de la caméra 5 est cliqué
        toggle_camera(5)


    pygame.display.flip()
    pygame.time.delay(100)  # Ajouter un léger délai pour éviter une utilisation intensive du CPU
