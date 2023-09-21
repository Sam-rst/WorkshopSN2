import pygame
from camera import CameraGroup
from save import SaveData
from dialog import DialogBox



all_sprites = pygame.sprite.Group()

projectile_sprites = pygame.sprite.Group()

ennemi_projectiles = pygame.sprite.Group()

items_drop = pygame.sprite.Group()

ennemi_group = pygame.sprite.Group()
pnj_group = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()
player = None
items_drop = pygame.sprite.Group()
items_sprites = pygame.sprite.Group()

#Messages
dialogues_caporal_intro = DialogBox('sarah', ["Blabla", "Blabla", "Blabla"])
dialogues_Emma_salon = DialogBox('emma', ["Bonjour Sarah je suis Emma.", "Je te guiderais tout au long de ton expédition !", "Bon courage."])
dialogues_Emma_teleporter = DialogBox('emma', ["Bienvenue !", "Tu te situe dans mon ordinateur", "Maintenant, tu vas te diriger vers la porte en bas...", "Ce sera l'entrée vers le firewall", "Je t'expliquerai à l'intérieur ta mission"])
dialogues_Emma_firewall_ferme = DialogBox('emma', ["Un des ordinateurs dans le fond est allumé, trouve le.", "Il va te permettre de trouver un port qui te permettra de rentrer dans le serveur", "Tu devras te connecter avec l'identifiant root...", "... c'est l'administrateur du serveur, il a tous les droits.", "Tentes de rentrer ces mots de passes : 1234, azerty, admin, root"])
dialogues_Emma_firewall_ouvert = DialogBox('emma', ["Tu as découvert quels ports sont ouverts...", "...vas voir lequel est ouvert"])
dialogues_Emma_server = DialogBox('emma', ["Tu as réussi à rentrer dans le serveur, bien joué !", "Maintenant tu vas tenter d'attaquer la base de données", "Pour cela tu vas chercher quelques indices parmi les différentes salles autour.", "Ce sont des réseaux, dont l'un possède la BDD", "Bonne chance !"])
dialogues_Emma_BDD = DialogBox('emma', ["Bien joué tu as trouvé le bon serveur !"])
dialogues_Emma_final = DialogBox('emma', ["Bravo, récupère ce parchemin"])


salon_collisions = pygame.sprite.Group()
teleporter_collisions = pygame.sprite.Group()
firewall_collisions = pygame.sprite.Group()
server_collisions = pygame.sprite.Group()
bdd_collisions = pygame.sprite.Group()
final_collisions = pygame.sprite.Group()

camera_groups = {
    "Salon": CameraGroup(name_map='Salon', list_teleporters=[('EntranceTeleporter', 'Teleporter', 'EntranceTeleporter')], layers_obstacles=(['Collisions'], salon_collisions), messages=dialogues_Emma_salon, name_interaction="AucuneInteraction"),
    "Teleporter": CameraGroup(name_map='Teleporter', list_teleporters=[('ExitTeleporter', 'Salon', 'ExitTeleporter'), ('EntranceFirewall', 'FirewallFerme', 'EntranceFirewall')], layers_obstacles=(['Collisions'], teleporter_collisions), messages=dialogues_Emma_teleporter, name_interaction="AucuneInteraction"),
    "FirewallFerme": CameraGroup(name_map='FirewallFerme', list_teleporters=[('ExitFirewall', 'Teleporter', 'ExitFirewall')], layers_obstacles=(['Collisions'], firewall_collisions), messages=dialogues_Emma_firewall_ferme, name_interaction="Terminal"),
    "FirewallOuvert": CameraGroup(name_map='FirewallOuvert', list_teleporters=[('ExitFirewall', 'Teleporter', 'ExitFirewall'), ('EntranceServer', 'Server', 'EntranceServer')], layers_obstacles=(['Collisions'], firewall_collisions), messages=dialogues_Emma_firewall_ouvert, name_interaction="AucuneInteraction"),
    "Server": CameraGroup(name_map='Server', list_teleporters=[('ExitServer', 'FirewallOuvert', 'ExitServer'), ('EntranceBDD', 'BDD', 'EntranceBDD')], layers_obstacles=(['Collisions'], server_collisions), messages=dialogues_Emma_server, name_interaction="BDD"),
    "BDD": CameraGroup(name_map='BDD', list_teleporters=[('ExitBDD', 'Server', 'ExitBDD'), ('EntranceFinal', 'FinalRoom', 'EntranceFinal')], layers_obstacles=(['Collisions'], bdd_collisions), messages=dialogues_Emma_BDD, name_interaction="AucuneInteraction"),
    "FinalRoom": CameraGroup(name_map='FinalRoom', list_teleporters=[('EntranceFinal', 'FinalRoom', 'EntranceFinal'), ('ExitFinal', 'BDD', 'ExitFinal')], layers_obstacles=(['Collisions'], final_collisions), messages=dialogues_Emma_final, name_interaction="Parchemin"),
}
# Water Fall ;)

save_data = SaveData('save.json')
map_name = save_data.load_player_map()
mob_dead = save_data.load_mob_dead()

if map_name is None:
    camera_group = camera_groups["Salon"]
else:
    camera_group = camera_groups[map_name]