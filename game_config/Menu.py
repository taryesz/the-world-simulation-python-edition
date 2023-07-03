import tkinter as tk


class Menu:

    def __init__(self, size, board_type, game):
        self.game = game
        self.size = size
        self.type = board_type
        self.__root = None
        self.__root_width = 500
        self.__root_height = 200
        self.__buttonHeight = int(self.__root_height * 0.5)
        self.__play_x = 0
        self.__board_size_x = 0
        self.__board_type_x = 0
        self.__load_game_x = 0
        self.__play_y = 0
        self.__board_size_y = self.__buttonHeight
        self.__board_type_y = 2 * self.__buttonHeight
        self.__load_game_y = 3 * self.__buttonHeight

    def createMenuObject(self):
        self.createWindow()
        self.createButtons()

    def createWindow(self):
        self.__root = tk.Tk()
        self.__root.title("The World Simulation")
        self.__root.geometry(f"{self.__root_width}x{self.__root_height}")
        self.__root.resizable(False, False)

    def createButtons(self):
        play = tk.Button(self.__root, text="Play", command=self.game.createGameObject)
        boardSize = tk.Button(self.__root, text="Choose the board size", command=self.size.createSizeObject)

        play.place(x=self.__play_x, y=self.__play_y, width=self.__root_width, height=self.__buttonHeight)
        boardSize.place(x=self.__board_size_x, y=self.__board_size_y, width=self.__root_width,
                        height=self.__buttonHeight)

        self.__root.mainloop()
