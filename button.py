import pygame, sys

class Button:
    def __init__(self, text, width, height, pos, elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.origin_y_pos = pos[1]
        
        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'
        
        # Bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#354B5E'
        
        # Text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self):
        # Elevation logic
        self.top_rect.y = self.origin_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed :
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'
        
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)

button1 = Button('Click me', 200, 40, (400, 200), 6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill('#DCDDD8')
    button1.draw()
    
    pygame.display.update()
    clock.tick(60)