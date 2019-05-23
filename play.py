# -*- coding: utf-8 -*-
from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
import globais

class Play(object):
    def __init__(self,window):
        self.window = window
        self.setNave()
        self.tie = []
        self.linha = []
        self.setInimigos()
        self.setLinhaInimigos()
        self.tiro = []
        self.cronometro = 0

    def setPlay(self):
        self.setDraw()
        self.setMovimento()
        self.setReturn()
        self.setTiroDado()
        self.getInimigos()

    def setNave(self):
        self.nave = Sprite("img/ywing.png")
        self.nave.set_position((globais.WIDTH/2) - self.nave.width/2, (globais.HEIGHT) - self.nave.height)

    def setMovimento(self):
        teclado = Keyboard()
        if (teclado.key_pressed("RIGHT") and (self.nave.x + self.nave.width - 15) < globais.WIDTH):
            self.nave.x += (globais.VEL_JOGADOR * self.window.delta_time())
        if (teclado.key_pressed("LEFT") and (self.nave.x + 15) > 0):
            self.nave.x -= (globais.VEL_JOGADOR * self.window.delta_time())
        if(teclado.key_pressed("SPACE")):
            if (self.cronometro <= 0):
                self.setTiro(self.nave.x + self.nave.width/2, self.nave.y + 20)
                self.cronometro = globais.RECARGA
        self.cronometro -= 1

    def setDraw(self):
        self.nave.draw()

    def setInimigos(self):
        self.tieU = Sprite("img/tie.png")

    def setLinhaInimigos(self):
        i=0
        j=0
        for i in range(1):
            for j in range(10):
                self.tieU.set_position(self.tieU.width*j, 10)
                self.tie.append(self.tieU)
            self.linha.append(self.tie)
            self.tie = []

    def getInimigos(self):
        for i in range(len(self.tie)):
            self.linha[i].draw()

    def setReturn(self):
        self.teclado = Keyboard()
        if(self.teclado.key_pressed("ESC")):
            globais.PAGINA_ATUAL = 0
        self.window.delay(100)

    def setTiro(self, inicial_x, inicial_y):
        tiro = Sprite("img/tiro.png")
        tiro.set_position(inicial_x, inicial_y)  
        self.tiro.append(tiro)

    def setTiroDado(self):
        if len(self.tiro) > 0:
            if self.tiro[-1].y + self.tiro[-1].height < 0:
                self.tiro = []
        for i in range(len(self.tiro)):
            self.tiro[i].y -= globais.VEL_TIRO * self.window.delta_time()
            self.tiro[i].draw()
