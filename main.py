import pygame, sys, time, math, introduction
from settings import *
import sprites
from debug import debug
from carte import Carte, Interaction
from player import *
from ennemy import *
from menu import MenuDebut, MenuFin
from items import Item
from pnj import *
from menu_marchand import *
from PHPMYADMIN import LoginPage
from terminal import CMD

pygame.init()

clock = pygame.time.Clock()

# Création des sprites

# Menus
login_page = LoginPage()
cmd = CMD()
menuDebut = MenuDebut()
menuFin = MenuFin()

# Saves
sprites.player = menuDebut.run()
last_save_time = pygame.time.get_ticks()

# Dialogues
emma = Emma("Emma", sprites.camera_group.carte.get_waypoint('SpawnEmmaSalon'), [sprites.camera_groups["Salon"], sprites.pnj_group], "Salon")
# Type camera
sprites.camera_group.set_type_camera("center")

last_time = time.time()
while True:
    dt = time.time() - last_time
    last_time = time.time()
    
    if sprites.player.is_teleporting:
        sprites.player.is_teleporting = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_position = {"x": sprites.player.pos.x, "y": sprites.player.pos.y}
            sprites.save_data.save_player_position(player_position)
            sprites.save_data.save_player_map(sprites.camera_group.carte.map_name)
            sprites.save_data.save_player_life(sprites.player.get_HP())
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                player_position = {"x": sprites.player.pos.x, "y": sprites.player.pos.y}
                sprites.save_data.save_player_position(player_position)
                sprites.save_data.save_player_map(sprites.camera_group.carte.map_name)
                sprites.save_data.save_player_life(sprites.player.get_HP())
                pygame.quit()
                sys.exit()

            for tp in sprites.camera_group.teleporters:
                if event.key == pygame.K_e and sprites.player.rect.colliderect(tp.rect):

                    name_dest = tp.name_destination
                    sprites.camera_group = sprites.camera_groups[name_dest]
                    sprites.player.set_pos(sprites.camera_groups[name_dest].carte.get_waypoint(tp.name_tp_back))
                    sprites.player.is_teleporting = True
            for sprite in sprites.items_drop:
                if event.key == pygame.K_a and sprites.player.rect.colliderect(sprite.rect):
                    sprite.remove_object(sprites.items_drop)

            if event.key == pygame.K_SPACE:
                sprites.camera_group.messages.execute()
                
            if event.key == pygame.K_a and sprites.player.rect.colliderect(sprites.camera_group.interaction.rect):
                if sprites.camera_group.interaction.name == "Terminal":
                    cmd.run()
                    if cmd.is_good:
                        sprites.camera_group = sprites.camera_groups["FirewallOuvert"]
                        sprites.camera_group.messages.open_dialog()
                    # Afficher le prochain message qui dis qu'un des ports est ouvert
                    
                elif sprites.camera_group.interaction.name == "BDD":
                    login_page.run()
                    # Afficher le prochain message qui dit que la prochaine salle se trouve dans le réseau n°3 au serveur n°13
                
                elif sprites.camera_group.interaction.name == "Parchemin":
                    menuFin.run()
                    # import subprocess

                    # # Exécuter le fichier Python en utilisant l'interpréteur Python
                    # subprocess.run(['python', 'menuFin.py'])
                    # Afficher le prochain message qui dit que la prochaine salle se trouve dans le réseau n°3 au serveur n°13

    if not sprites.camera_group.messages.reading:
        if pygame.sprite.spritecollide(sprites.player, sprites.pnj_group, False):
            sprites.camera_group.messages.open_dialog()
    
    # Background color depends of the map
    screen.fill('#000000')

    sprites.camera_group.update(dt)
    sprites.camera_group.custom_draw(sprites.player)

    sprites.camera_group.messages.render()
    
    # Sauvegarde la position du joueur toutes les 5 secondes
    current_time = pygame.time.get_ticks()
    if current_time - last_save_time > 5000:
        player_position = {"x": sprites.player.pos.x, "y": sprites.player.pos.y}
        sprites.save_data.save_player_position(player_position)
        sprites.save_data.save_player_map(sprites.camera_group.carte.map_name)
        sprites.save_data.save_player_life(sprites.player.get_HP())
        last_save_time = current_time
        

    # DEBUG : Permettre de faire apparaitre tous les sprites
    # sprites.camera_group.debug()

    pygame.display.update()
    clock.tick(60)

