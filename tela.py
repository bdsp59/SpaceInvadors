from PPlay.window import *
import globais
from menuSi import *
from playSi import *
from dificuldadeSi import *

def set_tela():
    tela = Window(globais.WIDTH,globais.HEIGHT)
    tela.set_title("Space Invadors")
    tela.set_background_color((0,0,0))

    while globais.GAME_STARTED:

        if(globais.GAME_STATE == 2):
            dificuldade = Dificuldade(tela)
            dificuldade.set_dificuldade()
            print(globais.GAME_STATE)
        elif(globais.GAME_STATE == 1):
            play = Play(tela)
            play.set_play()
            print(globais.GAME_STATE)
        elif(globais.GAME_STATE == 0):
            menu = Menu(tela)
            menu.set_menu()
            print(globais.GAME_STATE)
        
        tela.update()

if __name__ == "__main__":
    set_tela()