from abc import abstractmethod
from sprites.base.Organism import Organism


class Animal(Organism):

    def __init__(self, game, size):
        super().__init__(size, game)
        self.__size = size
        self.__game = game

    def action(self, x, y, organisms_copy):
        self.generateRandomCoordinates(x, y)

        x_position = x[0]
        y_position = y[0]

        self.draw(x_position, y_position, self.__size.get_ratio())

    @abstractmethod
    def createInstanceOfOrganism(self, game, size):
        pass
