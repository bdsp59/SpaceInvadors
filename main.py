from menu import Menu
from play import Play
from dificuldade import Dificuldade
from PPlay.window import Window
import globais

janela = Window(globais.WIDTH, globais.HEIGHT)
janela.set_title("Space Invadors")
janela.set_background_color((0,0,0))

menu = Menu(janela)
play = Play(janela)
dificuldade = Dificuldade(janela)

while globais.JOGO_RODANDO:
    janela.set_background_color((0,0,0))

    if(globais.PAGINA_ATUAL == 0):
        menu.setMenu()
    elif(globais.PAGINA_ATUAL == 1):
        play.setPlay()
    elif(globais.PAGINA_ATUAL == 2):
        dificuldade.setDificuldade()

    janela.update()
