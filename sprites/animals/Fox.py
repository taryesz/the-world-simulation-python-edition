from sprites.base.Animal import Animal


class Fox(Animal):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_power(3)
        self.set_initiative(7)
        self.set_name("fox")
        self.__game = game
        self.__size = size
        self.set_color("orange")

    def createInstanceOfOrganism(self, game, size):
        return Fox(game, size)

    def action(self, x, y, organisms_copy):
        self.generateRandomCoordinates(x, y)
        danger_detected = False

        x_position = x[0]
        y_position = y[0]

        organisms = self.__game.get_organisms()

        for organism in organisms:
            if x_position == organism.get_x_position() and y_position == organism.get_y_position():
                if organism.get_power() > self.get_power():
                    self.__game.appendMessage(f"<{self.get_name()}> doesn't want to get killed by "
                                              f"{organism.get_name()}.")
                    danger_detected = True

        if danger_detected:
            self.action(x, y, organisms_copy)
        else:
            self.draw(x_position, y_position, self.__size.get_ratio())
