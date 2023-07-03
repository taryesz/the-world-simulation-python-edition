from sprites.base.Animal import Animal
import random


class Antelope(Animal):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_power(4)
        self.set_initiative(4)
        self.set_name("antelope")
        self.__game = game
        self.__size = size
        self.set_color("brown")
        self.__step = self.__size.get_ratio() * 2

    def createInstanceOfOrganism(self, game, size):
        return Antelope(game, size)

    def collide(self, organisms_copy):
        for other_organism in self.__game.get_organisms():
            if self.get_index() is not other_organism.get_index():
                if self.get_x_position() == other_organism.get_x_position() and self.get_y_position() == other_organism.get_y_position() and (not self.get_collided_flag() and not other_organism.get_collided_flag()):
                    if other_organism.get_name() == "turtle" or other_organism.get_name() == "guarana":
                        other_organism.collide(organisms_copy)
                    else:
                        self.comparePowers(other_organism, organisms_copy)

    def comparePowers(self, other_organism, organisms_copy):
        if self.get_power() > other_organism.get_power():
            organisms_copy.remove(other_organism)
            self.__game.appendMessage(f"<{other_organism.get_name()}> died of {self.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        elif self.get_power() < other_organism.get_power():
            self.escape(organisms_copy, other_organism)
        else:
            self.compareInitiatives(other_organism, organisms_copy)

    def compareInitiatives(self, other_organism, organisms_copy):
        if self.get_initiative() > other_organism.get_initiative():
            organisms_copy.remove(self)
            self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        elif self.get_initiative() < other_organism.get_initiative():
            self.escape(organisms_copy, other_organism)
        else:
            self.spreadAnimals(other_organism, organisms_copy)

    def escape(self, organisms_copy, other_organism):
        chance = random.choice([True, False])

        if chance:
            x = [self.get_x_position()]
            y = [self.get_y_position()]
            self.generateRandomCoordinates(x, y)
            self.set_x_position(x[0])
            self.set_y_position(y[0])
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
            self.__game.appendMessage(f"<{self.get_name()}> managed to escape death.")
        else:
            organisms_copy.remove(self)
            self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)

    def generateRandomX(self, x):
        rand = random.Random()
        new_x = x[0] + self.__step if rand.randint(0, 1) == 0 else x[0] - self.__step
        if 0 <= new_x < self.__size.get_board_width() - self.__size.get_ratio():
            x[0] = new_x
        else:
            self.generateRandomX(x)

    def generateRandomY(self, y):
        rand = random.Random()
        new_y = y[0] + self.__step if rand.randint(0, 1) == 0 else y[0] - self.__step
        if 0 <= new_y < self.__size.get_board_height() - self.__size.get_ratio():
            y[0] = new_y
        else:
            self.generateRandomY(y)
