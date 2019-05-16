# _*_ coding: utf-8 _*_
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from dificuldade import *
from playSi import *
import globais
class Menu(object):

    def __init__(self,window):
        self.window = window
        self.set_menu()

    def set_menu(self):
        Window.draw_text(self.window,"Space Invadors", 7*(globais.WIDTH/32), (globais.HEIGHT)/16, size=70, color = (100,100,100), font_name = "Arial", bold = False, italic = False) 
        self.get_draw()
        self.set_close()

    def set_play(self):
        self.play = Sprite("PLAY.png")
        self.play.x = ((globais.WIDTH/4))
        self.play.y = ((globais.HEIGHT/2) - (globais.HEIGHT/8))
        if(self.mouse.is_over_object(self.play)):
            if(self.mouse.is_button_pressed(1)):
                globais.GAME_STATE = 1
    
    def get_draw(self):
        self.set_mouse()
        self.set_play()
        self.set_dificuldade()
        self.set_rank()
        self.set_quit()
        self.play.draw()
        self.dificuldade.draw()
        self.rank.draw()
        self.quit.draw()

    def set_dificuldade(self):
        self.dificuldade = Sprite("DIFICULDADE.png")
        self.dificuldade.x = ((globais.WIDTH/2) + (globais.WIDTH/8))
        self.dificuldade.y = 3*(globais.HEIGHT/8)

        if(self.mouse.is_over_object(self.dificuldade)):
            if(self.mouse.is_button_pressed(1)):
                globais.GAME_STATE = 2

    def set_rank(self):
        self.rank = Sprite("RANK.png")
        self.rank.x = ((globais.WIDTH/4))
        self.rank.y = ((globais.HEIGHT/2) + (globais.HEIGHT/8)) 
    
    def set_quit(self):
        self.quit = Sprite("QUIT.png")
        self.quit.x = ((globais.WIDTH/2) + (globais.WIDTH/8))
        self.quit.y = ((globais.HEIGHT/2) + (globais.HEIGHT/8))

    def set_mouse(self):
        self.mouse = Window.get_mouse()

    def set_close(self):
        teclado = Window.get_keyboard()
        if(teclado.key_pressed("ESC")):
            globais.GAME_STARTED = False

'''
    Criar a tela MENU do Space Invadors -> teremos que desenvolver uma tela com os seguintes elementos: PLAY, DIFICULDADE, RANK, QUIT.
    Os elementos devem ser clicados e quando cada um for clicado deve ser enviado para uma tela relacionada com o que cada tecla faz.
        -Ao clicar em PLAY deve aparecer uma janela preta, neste momento, e quando for pressionado a tecla ESC deve retornar a tela MENU;
        -Ao clicar em DIFICULDADE deve aparecer uma tela com três botões: FÁCIL, MÉDIO, DIFÍCIL. Ao clicar em um desses botões uma variável global "Dificuldade"
        deve ser alterada de modo a influciar em elementos do jogo. A tecla ESC deve retornar ao MENU(só essa obrigatória) e a tecla ENTER deve iniciar o jogo; 
        -RANK ainda não deve fazer nada
        -QUIT encerra o jogo

        (mouse.get_position[1]() >= play.x) and (mouse.get_position[1]() <= play.x+play.width) and (mouse.get_position()[1] >= play.y) and (mouse.get_position()[1] <= play.y+play.height)
'''