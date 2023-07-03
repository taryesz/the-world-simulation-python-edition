from sprites.base.Animal import Animal


class Wolf(Animal):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_power(9)
        self.set_initiative(5)
        self.set_name("wolf")
        self.__game = game
        self.__size = size
        self.set_color("gray")

    def createInstanceOfOrganism(self, game, size):
        return Wolf(game, size)
