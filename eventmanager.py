import sys
import pygame as pg
from bullet import Bullet

#Linux OP
class EventManager:
    def __init__(self, game):
        self.game = game

    #Main EventManager controller
    def get_event_input(self):
        for e in pg.event.get():  #listen for keyboard
            if e.type == pg.QUIT: #if (x) is hit in window
                print("Exiting game . . .")
                sys.exit()

            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    sys.exit()
                elif e.key == pg.K_SPACE:
                    self.fire_bullet()
                self.move_player(e) #Player move

            elif e.type == pg.KEYUP:
                self.stop_player(e)
    
    #Directional keys on
    def move_player(self, event):
        if event.key == pg.K_d:  #right
            self.game.ship.horiz = 1
        elif event.key == pg.K_a: #left
            self.game.ship.horiz = -1
        if event.key == pg.K_w: #Up
            self.game.ship.vert = -1
        elif event.key == pg.K_s: #down
            self.game.ship.vert = 1

    #Directional keys off
    def stop_player(self,event):
        if(event.key == pg.K_d or event.key == pg.K_a):
            self.game.ship.horiz = 0
        if(event.key == pg.K_s or event.key == pg.K_w):
            self.game.ship.vert = 0

    def fire_bullet(self):
        pass
        new_bullet = Bullet(self.game)
        self.game.bullets.add(new_bullet) #add to games bullet group
#end of EventManager
