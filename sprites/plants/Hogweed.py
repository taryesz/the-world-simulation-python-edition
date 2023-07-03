import sys

from sprites.base.Plant import Plant


class Hogweed(Plant):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_name("hogweed")
        self.__game = game
        self.__size = size
        self.set_color("red")
        self.set_power(10)

    def createInstanceOfOrganism(self, game, size):
        return Hogweed(game, size)

    def action(self, x, y, organisms_copy):
        for i in range(len(self.__game.get_organisms())):

            other_x = self.__game.get_organisms()[i].get_x_position()
            other_y = self.__game.get_organisms()[i].get_y_position()

            left = (other_x == self.get_x_position() - self.__size.get_ratio() and other_y == self.get_y_position())
            right = (other_x == self.get_x_position() + self.__size.get_ratio() and other_y == self.get_y_position())
            top = (other_x == self.get_x_position() and other_y == self.get_y_position() - self.__size.get_ratio())
            bottom = (other_x == self.get_x_position() and other_y == self.get_y_position() + self.__size.get_ratio())

            deletion = [left, right, top, bottom]

            for j in range(4):
                if deletion[j] and i < len(organisms_copy):
                    if self.__game.get_organisms()[i].get_name() == "cyber":
                        pass
                    else:
                        if not self.__game.get_organisms()[i].get_ability_flag():
                            self.__game.appendMessage(
                                f"<{self.__game.get_organisms()[i].get_name()}> died of {self.get_name()}")
                            self.set_collided_flag(True)
                            self.__game.get_organisms()[i].set_collided_flag(True)
                            if organisms_copy[i].get_name() == "human":
                                sys.exit(0)
                            organisms_copy.pop(i)
                        else:
                            self.__game.appendMessage("<player> cannot get killed while ability enabled")

        self.draw(x[0], y[0], self.__size.get_ratio())

    def collide(self, organisms_copy):
        for other_organism in self.__game.get_organisms():
            if self.get_index() is not other_organism.get_index():
                if self.get_x_position() == other_organism.get_x_position() and self.get_y_position() == other_organism.get_y_position() and (not self.get_collided_flag() and not other_organism.get_collided_flag()):
                    if other_organism.get_name() == "cyber":
                        print("yes")
                        organisms_copy.remove(self)
                        self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")
                        self.set_collided_flag(True)
                        other_organism.set_collided_flag(True)
                    else:
                        self.comparePowers(other_organism, organisms_copy)
