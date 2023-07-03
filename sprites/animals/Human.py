import sys

from sprites.base.Animal import Animal


class Human(Animal):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_power(5)
        self.set_initiative(4)
        self.set_name("human")
        self.__game = game
        self.__size = size
        self.rgb = (42, 76, 89)
        self.set_color("#%02x%02x%02x" % (self.rgb[0], self.rgb[1], self.rgb[2]))

    def createInstanceOfOrganism(self, game, size):
        return Human(game, size)

    def action(self, x, y, organisms_copy):
        if self.get_key() == "left":  # Left arrow key
            if not x[0] - self.__size.get_ratio() < 0:
                x[0] = x[0] - self.__size.get_ratio()
        elif self.get_key() == "right":  # Right arrow key
            if not x[0] + self.__size.get_ratio() > self.__size.get_board_width() - self.__size.get_ratio():
                x[0] = x[0] + self.__size.get_ratio()
        elif self.get_key() == "up":  # Up arrow key
            if not y[0] - self.__size.get_ratio() < 0:
                y[0] = y[0] - self.__size.get_ratio()
        elif self.get_key() == "down":  # Down arrow key
            if not y[0] + self.__size.get_ratio() > self.__size.get_board_height() - self.__size.get_ratio():
                y[0] = y[0] + self.__size.get_ratio()

        self.draw(x[0], y[0], self.__size.get_ratio())

    def collide(self, organisms_copy):
        for other_organism in self.__game.get_organisms():
            if self.get_index() is not other_organism.get_index():
                if self.get_x_position() == other_organism.get_x_position() and self.get_y_position() == other_organism.get_y_position() and (not self.get_collided_flag() and not other_organism.get_collided_flag()):
                    if other_organism.get_name() == "turtle" or other_organism.get_name() == "guarana" or other_organism.get_name() == "antelope":
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
            if self.get_ability_flag():
                self.activateAbility()
            else:
                organisms_copy.remove(self)
                self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")
                sys.exit(0)
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        else:
            self.compareInitiatives(other_organism, organisms_copy)

    def compareInitiatives(self, other_organism, organisms_copy):
        if self.get_initiative() > other_organism.get_initiative():
            if self.get_ability_flag():
                self.activateAbility()
            else:
                organisms_copy.remove(self)
                self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")
                sys.exit(0)
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        elif self.get_initiative() < other_organism.get_initiative():
            organisms_copy.remove(other_organism)
            self.__game.appendMessage(f"<{other_organism.get_name()}> died of {self.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)

    def activateAbility(self):
        x = [self.get_x_position()]
        y = [self.get_y_position()]
        self.generateRandomCoordinates(x, y)
        self.set_x_position(x[0])
        self.set_y_position(y[0])
        self.__game.appendMessage("<player> cannot get killed while ability enabled")
