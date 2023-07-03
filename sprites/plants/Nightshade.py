from sprites.base.Plant import Plant


class Nightshade(Plant):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_name("nightshade")
        self.__game = game
        self.__size = size
        self.set_color("purple")
        self.set_power(99)

    def createInstanceOfOrganism(self, game, size):
        return Nightshade(game, size)
