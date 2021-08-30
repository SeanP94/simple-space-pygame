import pygame as pg
import pygame.sprite as Sprite


class Bullet(Sprite):
    def __init__(self,game):
        super().__init__() #Will be called at ships location
        self.screen = game.screen
        self.settings = game.settings
        #self.color = self.settings.bullet_color
        self.rect = pg.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.mid.top #Shoots out of the middle center of ship
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)