from sprites.base.Organism import Organism
from abc import abstractmethod
import random


class Plant(Organism):
    
    def __init__(self, game, size):
        super().__init__(size, game)
        self.set_initiative(0)
        self.set_power(0)
        self.set_is_plant_flag(True)
        self.__game = game
        self.__size = size
        self.__attempts = 3

    def action(self, x, y, organisms_copy):
        self.draw(x[0], y[0], self.__size.get_ratio())
        random1 = random.Random()
        try1 = random1.randint(0, 800)

        attempts = 0
        while attempts < self.__attempts and try1 == 0:
            for i in range(len(self.__game.get_organisms())):

                other_x = self.__game.get_organisms()[i].get_x_position()
                other_y = self.__game.get_organisms()[i].get_y_position()

                left = (other_x == self.get_x_position() - self.__size.get_ratio() and other_y == self.get_y_position())
                right = (other_x == self.get_x_position() + self.__size.get_ratio() and other_y == self.get_y_position())
                top = (other_x == self.get_x_position() and other_y == self.get_y_position() - self.__size.get_ratio())
                bottom = (other_x == self.get_x_position() and other_y == self.get_y_position() + self.__size.get_ratio())
                adjacent = (left and right and top and bottom)

                if not adjacent:
                    target = random.Random()
                    targetR = target.randint(0, 3)
                    where_to_x = 0
                    where_to_y = 0
                    if targetR == 0 and not left:
                        where_to_x = -self.__size.get_ratio()
                        where_to_y = 0
                    elif targetR == 1 and not right:
                        where_to_x = self.__size.get_ratio()
                        where_to_y = 0
                    elif targetR == 2 and not top:
                        where_to_x = 0
                        where_to_y = -self.__size.get_ratio()
                    elif targetR == 3 and not bottom:
                        where_to_x = 0
                        where_to_y = self.__size.get_ratio()

                    self.multiply(where_to_x, where_to_y)
                    break

            attempts += 1

    def multiply(self, x, y):
        x_position = self.get_x_position() + x
        y_position = self.get_y_position() + y

        if (0 <= y_position < self.__size.get_board_height() - self.__size.get_ratio()) and (0 <= x_position < self.__size.get_board_width()):
            new_organism = self.createInstanceOfOrganism(self.__game, self.__size)

            if new_organism is not None:
                new_organism.set_x_position(x_position)
                new_organism.set_y_position(y_position)
                new_organism.set_age(1)

                new_organism.set_collided_flag(True)

                self.__game.addOrganismToOrganismsList(new_organism)

    @abstractmethod
    def createInstanceOfOrganism(self, game, size):
        pass
