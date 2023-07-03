from sprites.base.Animal import Animal
import random


class Turtle(Animal):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.__critical_power = 5
        self.set_power(2)
        self.set_initiative(1)
        self.set_name("turtle")
        self.__game = game
        self.__size = size
        self.set_color("blue")

    def createInstanceOfOrganism(self, game, size):
        return Turtle(game, size)

    def action(self, x, y, organisms_copy):
        desire_to_move = random.randint(0, 99)

        if desire_to_move > 75:
            self.generateRandomCoordinates(x, y)
            self.draw(x[0], y[0], self.__size.get_ratio())
        else:
            self.draw(x[0], y[0], self.__size.get_ratio())

    def collide(self, organisms_copy):
        for other_organism in self.__game.get_organisms():
            if self.get_index() is not other_organism.get_index():
                if self.get_x_position() == other_organism.get_x_position() and self.get_y_position() == other_organism.get_y_position() and (not self.get_collided_flag() and not other_organism.get_collided_flag()):
                    self.comparePowers(other_organism, organisms_copy)

    def comparePowers(self, other_organism, organisms_copy):
        if self.get_power() > other_organism.get_power():
            organisms_copy.remove(other_organism)
            self.__game.appendMessage(f"<{other_organism.get_name()}> died of {self.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        elif self.get_power() < other_organism.get_power():
            self.resist(organisms_copy, other_organism)
        else:
            self.compareInitiatives(other_organism, organisms_copy)

    def compareInitiatives(self, other_organism, organisms_copy):
        if self.get_initiative() > other_organism.get_initiative():
            organisms_copy.remove(self)
            self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        elif self.get_initiative() < other_organism.get_initiative():
            self.resist(organisms_copy, other_organism)
        else:
            self.spreadAnimals(other_organism, organisms_copy)

    def resist(self, organisms_copy, other_organism):
        if other_organism.get_power() < self.__critical_power:
            other_organism.set_x_position(other_organism.get_prev_x_position())
            other_organism.set_y_position(other_organism.get_prev_y_position())

            self.__game.appendMessage(f"<{other_organism.get_name()}> was kicked away by the turtle. "
                                      f"Old coords ({other_organism.get_prev_x_position()}, {other_organism.get_prev_y_position()}); "
                                      f"New coords ({other_organism.get_x_position()}, {other_organism.get_y_position()})")
        else:
            organisms_copy.remove(self)
            self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")

        self.set_collided_flag(True)
        other_organism.set_collided_flag(True)
