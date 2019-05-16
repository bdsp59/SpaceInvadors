# _*_ coding: utf-8 _*_
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from menuSi import *
import globais

pygame.init()

class Dificuldade(object):
    def __init__(self,window):
        self.window = window
        self.set_dificuldade()
    
    def set_dificuldade(self):
        Window.draw_text(self.window,"Escolha a Dificuldade", (3)*(globais.WIDTH/32), (globais.HEIGHT)/16, size=70, color = (100,100,100), font_name = "Arial", bold = False, italic = False)
        self.set_facil()
        self.get_facil_draw()
        self.set_medio()
        self.get_medio_draw()
        self.set_dificil()
        self.get_dificil_draw()
        self.set_nivel_dificuldade()

    def get_facil(self):
        return self.facil
    
    def get_medio(self):
        return self.medio
    
    def get_dificil(self):
        return self.dificil

    def set_facil(self):
        self.facil = Sprite("FACIL.png")
        self.facil.x = ((2.1)*(globais.WIDTH/5))
        self.facil.y = (2*(globais.HEIGHT/6))
    
    def get_facil_draw(self):
        self.facil.draw()

    def set_medio(self):
        self.medio = Sprite("MEDIO.png")
        self.medio.x = ((2.1)*(globais.WIDTH/5))
        self.medio.y = (3*(globais.HEIGHT/6))
    
    def get_medio_draw(self):
        self.medio.draw()

    def set_dificil(self):
        self.dificil = Sprite("DIFICIL.png")
        self.dificil.x = ((2.1)*(globais.WIDTH/5))
        self.dificil.y = (4*(globais.HEIGHT/6))
    
    def get_dificil_draw(self):
        self.dificil.draw()

    def set_close(self):
        teclado = Window.get_keyboard()
        if(teclado.key_pressed("ESC")):
            globais.GAME_STATE = 0

    def set_nivel_dificuldade(self):
        mouse = self.window.get_mouse()
        if(mouse.is_over_object(self.get_facil())):
            if(mouse.is_button_pressed(1)):
                globais.DIFICULTY = 1
        elif(mouse.is_over_object(self.get_medio())):
            if(mouse.is_button_pressed(1)):
                globais.DIFICULTY = 2
        elif(mouse.is_over_object(self.get_dificil())):
            if(mouse.is_button_pressed(1)):
                globais.DIFICULTY = 3 