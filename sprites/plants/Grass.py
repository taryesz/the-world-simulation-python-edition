from sprites.base.Plant import Plant


class Grass(Plant):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_name("grass")
        self.__game = game
        self.__size = size
        self.set_color("green")

    def createInstanceOfOrganism(self, game, size):
        return Grass(game, size)
