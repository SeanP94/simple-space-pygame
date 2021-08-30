import os.path      #os.path is file location
import pygame as pg #game library
import eventmanager as em
import player as p
import settings

class SpaceGame:
    def __init__(self):
        #Game settings
        self.settings = settings.Settings()
        #Init PyGame Objects
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        #FULLSCREEN
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        
        #Init my objects.
        self.ship = p.Ship(self)
        self.evm = em.EventManager(self)

    def run_game(self):
        #game run
        while True:     #endless loop, until exit, comes from update
            self.update()
            self.draw()
    
    def update(self):
        self.evm.get_event_input()
        self.ship.update()

    def draw(self):
        #Background
        self.screen.fill(self.settings.bg_color) #sets color of screen
        #Background Objects
        #enemies
        #Player
        self.ship.draw()
        pg.display.flip() #Show most recent drawn screen

#end of SpaceGame

