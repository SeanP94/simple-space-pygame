import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,game):
        self.game = game
        super().__init__() #Will be called at ships location 
        self.screen = game.screen
        self.settings = game.settings
        #self.color = self.settings.bu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 llet_color
        self.rect = pg.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop #Shoots out of the middle center of ship
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed #Moves forward
        self.rect.y = self.y

    def draw(self):
        pg.draw.rect(self.screen, self.settings.bullet_color, self.rect)