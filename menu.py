# -*- coding: utf-8 -*-
from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
import globais

class Menu(object):
    def __init__(self, window):
        self.window = window 
        #Aqui vamos declarar que a variavel window criada no main.py será enviada ao menu.py, de modo que ela seja igual a janela criada

    def setMenu(self):
        #'Nesta parte irá rodar a página menu, teremos outras defs para criar e desenhar os Sprites, mas é nesta def que vamos colocar o que realmente deve rodar no programa'
        self.setBotoes()
        self.setDraw()
        self.setClique()
        self.setReturn()

    def setBotoes(self):
        #'Nesta parte vamos criar todos os sprites e definir suas posições na janela'
        self.play = Sprite("img/PLAY.png")
        self.play.set_position(((2*globais.WIDTH/5) - self.play.width), ((globais.HEIGHT/2) - self.play.height))
        self.dificuldade = Sprite("img/DIFICULDADE.png")
        self.dificuldade.set_position(((4*globais.WIDTH/5) - self.play.width), ((globais.HEIGHT/2) - self.play.height))
        self.rank = Sprite("img/RANK.png")
        self.rank.set_position(((2*globais.WIDTH/5) - self.rank.width), ((globais.HEIGHT/2) + self.rank.height))
        self.quit = Sprite("img/QUIT.png")
        self.quit.set_position(((4*globais.WIDTH/5) - self.quit.width), ((globais.HEIGHT/2) + self.quit.height))

    def setDraw(self):
        #'Nesta parte vamos desenhar todos os sprites que criamos no setBotoes(), mas antes temos que chamar o setBotoes dentro do setDraw para que ele crie as Sprites'
        self.window.draw_text("Space Invaders", globais.WIDTH/4, globais.HEIGHT/4, size = 60, color = (255,255,255),font_name="Arial", bold=True, italic=False)
        self.play.draw()
        self.dificuldade.draw()
        self.rank.draw()
        self.quit.draw()

    def setClique(self):
        self.mouse = Mouse()
        if(self.mouse.is_over_object(self.play)):
            if(self.mouse.is_button_pressed(1)):
                globais.PAGINA_ATUAL = 1
        if(self.mouse.is_over_object(self.dificuldade)):
            if(self.mouse.is_button_pressed(1)):
                globais.PAGINA_ATUAL = 2
        if(self.mouse.is_over_object(self.rank)):
            if(self.mouse.is_button_pressed(1)):
                print("RANK")
        if(self.mouse.is_over_object(self.quit)):
            if(self.mouse.is_button_pressed(1)):
                globais.JOGO_RODANDO = False

    def setReturn(self):
        self.teclado = Keyboard()
        if(self.teclado.key_pressed("ESC")):
            globais.JOGO_RODANDO = False