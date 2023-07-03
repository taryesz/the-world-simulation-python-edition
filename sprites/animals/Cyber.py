from sprites.base.Animal import Animal


class Cyber(Animal):

    def __init__(self, game, size):
        super().__init__(game, size)
        self.set_power(11)
        self.set_initiative(4)
        self.set_name("cyber")
        self.__game = game
        self.__size = size
        self.set_color("lightblue")

    def createInstanceOfOrganism(self, game, size):
        return Cyber(game, size)

    def action(self, x, y, organisms_copy):

        hogweed_list = []

        for organism in self.__game.get_organisms():
            if organism.get_name() == "hogweed":
                hogweed_list.append(organism)

        if len(hogweed_list) > 0:

            closest_hogweed = None
            closest_distance = float('inf')

            for hogweed in hogweed_list:
                distance = self.calculate_distance(x[0], y[0], hogweed.get_x_position(), hogweed.get_y_position())
                if distance < closest_distance:
                    closest_distance = distance
                    closest_hogweed = hogweed

            if closest_hogweed is not None:
                hogweed_x = closest_hogweed.get_x_position()
                hogweed_y = closest_hogweed.get_y_position()

                dx = hogweed_x - x[0]
                dy = hogweed_y - y[0]

                if abs(dx) > abs(dy):
                    if dx > 0:
                        x[0] += self.__size.get_ratio()
                    elif dx < 0:
                        x[0] -= self.__size.get_ratio()
                else:
                    if dy > 0:
                        y[0] += self.__size.get_ratio()
                    elif dy < 0:
                        y[0] -= self.__size.get_ratio()

                self.draw(x[0], y[0], self.__size.get_ratio())
        else:
            super().action(x, y, organisms_copy)

    def calculate_distance(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
