from sprites.base.Animal import Animal


class Sheep(Animal):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_power(4)
        self.set_initiative(4)
        self.set_name("sheep")
        self.__game = game
        self.__size = size
        self.set_color("black")

    def createInstanceOfOrganism(self, game, size):
        return Sheep(game, size)
