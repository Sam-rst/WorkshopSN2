import pygame
from settings import *

class DialogBox:
    
    X_POSITION = 200
    Y_POSITION = screen.get_height() - 200
    
    def __init__(self, nom_perso, texts):
        self.nom_perso = nom_perso
        self.box = pygame.image.load('graphics/dialog/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (1200, 150))
        self.pnj = pygame.image.load(f'graphics/caracters/{self.nom_perso}/right/sprite_1.png')
        self.pnj = pygame.transform.scale(self.pnj, (100, 150))
        self.texts = texts
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font('graphics/font/Cyberpunk2.ttf', 30)
        self.reading = False
        self.was_speak = False
        
    def open_dialog(self):
        self.reading = True
        self.text_index = 0
    
    def execute(self):
        self.next_text()
        
    def render(self):
        if self.reading:
            self.letter_index += 1
            
            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index
            
            screen.blit(self.box, (self.X_POSITION, self.Y_POSITION))
            screen.blit(self.pnj, (self.X_POSITION-100, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 100, self.Y_POSITION + 20))
        
    def next_text(self):
        self.text_index += 1
        self.letter_index = 0
        
        if self.text_index >= len(self.texts):
            self.reading = False