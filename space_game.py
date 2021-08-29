import sys
import os.path      #os.path is file location
import pygame as pg #game library

class SpaceGame:
    def __init__(self):
        #Game settings
        self.settings = Settings()
        #Init PyGame Objects
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #Init my objects.
        self.ship = Ship(self)
        self.evm = EventManager()

    def run_game(self):
        #game run
        while True:                   #endless loop, until exit
            self.evm.get_event_input()
            #Background
            self.screen.fill(self.settings.bg_color) #
            #Background Objects
            #enemies
            #Player
            self.ship.draw()
            
            pg.display.flip() #Show most recent drawn screen

    #end of SpaceGame

class EventManager:
    def get_event_input(self):
        for e in pg.event.get():  #listen for keyboard
            if e.type == pg.QUIT: #if (x) is hit in window
                print("Exiting game . . .")
                sys.exit()
            #if e.type == pg.K_a:
                #print('a')

    #end of EventManager

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
#end of Settings

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect() #kid
        #Load image and rectangle
        self.image = pg.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        #indicate start position in game when amde
        self.rect.midbottom = self.screen_rect.midbottom
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
#end of Ship