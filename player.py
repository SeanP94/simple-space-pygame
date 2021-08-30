import pygame as pg #game library

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() 
        #Load image and rectangle
        self.image = pg.image.load('assets/ship.png')
        self.rect = self.image.get_rect()
        #indicate start position in game when amde
        self.rect.center = self.screen_rect.center
        self.rect 
        #Variables
        self.speed = 1.5
        self.horiz = 0 # -1 left, 1 right 
        self.vert = 0  # -1 down 1 up
    
    def update(self):
        self.x = round(self.horiz * self.speed)
        self.y = round(self.vert * self.speed)

        if(self.rect.right < self.screen_rect.right and self.horiz == 1):
            self.rect.x += self.x
        elif(self.rect.left > self.screen_rect.left and self.horiz == -1):
            self.rect.x += self.x
        if(self.rect.top > self.screen_rect.top and self.vert == -1):
            self.rect.y += self.y
        elif(self.rect.bottom < self.screen_rect.bottom and self.vert == 1):
            self.rect.y += self.y
        #dprint(str(self.x) +"  "+str(self.y))
    def draw(self):
        self.screen.blit(self.image, self.rect)

#end of Ship
