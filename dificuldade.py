# -*- coding: utf-8 -*-
from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
import globais

class Dificuldade(object):
    def __init__(self,window):
        self.window = window
    
    def setDificuldade(self):
        self.setBotoes()
        self.setDraw()
        self.setClique()
        self.setReturn()

    def setBotoes(self):
        self.facil = Sprite("img/FACIL.png")
        self.facil.set_position((globais.WIDTH/2) - (self.facil.width/2), (3*(globais.HEIGHT/7)) )
        self.medio = Sprite("img/MEDIO.png")
        self.medio.set_position((globais.WIDTH/2) - (self.medio.width/2), (4*(globais.HEIGHT/7)) )
        self.dificil = Sprite("img/DIFICIL.png")
        self.dificil.set_position((globais.WIDTH/2) - (self.dificil.width/2), (5*(globais.HEIGHT/7)) )

    def setDraw(self):
        self.window.draw_text("Escolha a dificuldade:", (3*globais.WIDTH/9), (2*(globais.HEIGHT/7)), size = 30, color = (255,255,255),font_name="Arial", bold=True, italic=False)
        self.facil.draw()
        self.medio.draw()
        self.dificil.draw()

    def setClique(self):
        self.mouse = Mouse()
        if(self.mouse.is_over_object(self.facil)):
            if(self.mouse.is_button_pressed(1)):
                globais.DIFICULDADE = 1
                globais.PAGINA_ATUAL = 0
        if(self.mouse.is_over_object(self.medio)):
            if(self.mouse.is_button_pressed(1)):
                globais.DIFICULDADE = 2
                globais.PAGINA_ATUAL = 0
        if(self.mouse.is_over_object(self.dificil)):
            if(self.mouse.is_button_pressed(1)):
                globais.DIFICULDADE = 3
                globais.PAGINA_ATUAL = 0

    def setReturn(self):
        self.teclado = Keyboard()
        if(self.teclado.key_pressed("ESC")):
            globais.PAGINA_ATUAL = 0
        self.window.delay(100)