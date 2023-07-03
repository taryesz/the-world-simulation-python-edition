from sprites.base.Plant import Plant


class Guarana(Plant):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_name("guarana")
        self.__game = game
        self.__size = size
        self.set_color("pink")
        self.__power_incrementation = 3

    def createInstanceOfOrganism(self, game, size):
        return Guarana(game, size)

    def collide(self, organisms_copy):
        for other_organism in self.__game.get_organisms():
            if self.get_index() is not other_organism.get_index():
                if self.get_x_position() == other_organism.get_x_position() and self.get_y_position() == other_organism.get_y_position() and (
                        not self.get_collided_flag() and not other_organism.get_collided_flag()):
                    self.comparePowers(other_organism, organisms_copy)

    def comparePowers(self, other_organism, organisms_copy):
        if self.get_power() > other_organism.get_power():
            organisms_copy.remove(other_organism)
            self.__game.appendMessage(f"<{other_organism.get_name()}> died of {self.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        elif self.get_power() < other_organism.get_power():
            organisms_copy.remove(self)
            self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}. Increasing creature's power from {other_organism.get_power()} to {self.__power_incrementation + other_organism.get_power()}")
            other_organism.set_power(self.__power_incrementation + other_organism.get_power())
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        else:
            self.compareInitiatives(other_organism, organisms_copy)

    def compareInitiatives(self, other_organism, organisms_copy):
        if self.get_initiative() > other_organism.get_initiative():
            organisms_copy.remove(self)
            self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}. Increasing creature's power from {other_organism.get_power()} to {self.__power_incrementation + other_organism.get_power()}")
            other_organism.set_power(self.__power_incrementation + other_organism.get_power())
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        elif self.get_initiative() < other_organism.get_initiative():
            organisms_copy.remove(other_organism)
            self.__game.appendMessage(f"<{other_organism.get_name()}> died of {self.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
