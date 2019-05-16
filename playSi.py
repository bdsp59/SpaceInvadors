# _*_ coding: utf-8 _*_
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import globais
from tela import *

pygame.init()

class Play(object):
    def __init__(self,window):
        self.window = window
        self.set_play()

    def set_play(self):
        self.set_close()

    def set_close(self):
        teclado = Window.get_keyboard()
        if(teclado.key_pressed("ESC")):
            globais.GAME_STATE = 0