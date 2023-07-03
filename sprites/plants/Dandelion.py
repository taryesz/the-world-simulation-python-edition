from sprites.base.Plant import Plant


class Dandelion(Plant):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_name("dandelion")
        self.__game = game
        self.__size = size
        self.set_color("yellow")

    def createInstanceOfOrganism(self, game, size):
        return Dandelion(game, size)
