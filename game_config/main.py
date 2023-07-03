from Menu import Menu
from Size import Size
from Type import Type
from Game import Game


size = Size()
board_type = Type()
game = Game(size)
menu = Menu(size, board_type, game)
menu.createMenuObject()
