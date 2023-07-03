import random
from abc import ABC, abstractmethod


class Organism(ABC):

    def __init__(self, size, game):
        self.__collided_flag = None
        self.__y_position_prev = None
        self.__x_position_prev = None
        self.__game = game
        self.__name = None
        self.__initiative = None
        self.__power = None
        self.__organisms_copy = game.get_organisms_copy()
        self.__index = []
        self.__age = None
        self.__y_position = 0
        self.__x_position = 0
        self.__size = size
        self.__color = None
        self.__is_plant_flag = False
        self.__key = None
        self.__ability_flag = False
        self.__timer = -1
        self.__cool_down = False

    # main functions:

    def generateRandomX(self, x):
        rand = random.Random()
        ratio = self.__size.get_ratio()
        new_x = x[0] + ratio if rand.randint(0, 1) == 0 else x[0] - ratio
        if self.__size.get_board_width() - ratio > new_x >= 0 and new_x % ratio == 0:
            x[0] = new_x
        else:
            self.generateRandomX(x)

    def generateRandomY(self, y):
        rand = random.Random()
        ratio = self.__size.get_ratio()
        new_y = y[0] + ratio if rand.randint(0, 1) == 0 else y[0] - ratio
        if self.__size.get_board_height() - ratio > new_y >= 0 and new_y % ratio == 0:
            y[0] = new_y
        else:
            self.generateRandomY(y)

    def generateRandomCoordinates(self, x, y):
        rand = random.Random()
        modify_x_y = rand.choice([True, False])

        if modify_x_y:
            self.generateRandomX(x)
        else:
            self.generateRandomY(y)

    def initializeOrganisms(self, organism, index, human):
        number_of_organisms = 1 if human else random.randint(2, 3)
        ratio = self.__size.get_ratio()
        board_width = self.__size.get_board_width()
        board_height = self.__size.get_board_height()

        for i in range(number_of_organisms):
            random_x_position = random.randint(ratio, board_width - ratio)
            random_y_position = random.randint(ratio, board_height - ratio)

            random_x_position = random_x_position // ratio * ratio
            random_y_position = random_y_position // ratio * ratio

            new_organism = self.createInstanceOfOrganism(self.__game, self.__size)

            if new_organism is not None:
                new_organism.set_x_position(random_x_position)
                new_organism.set_y_position(random_y_position)
                new_organism.set_age(1)
                new_organism.set_index(index[0])
                index[0] += 1

                self.__game.addOrganismToOrganismsList(new_organism)

    def collide(self, organisms_copy):
        for other_organism in self.__game.get_organisms():
            if self.get_index() is not other_organism.get_index():
                if self.get_x_position() == other_organism.get_x_position() and self.get_y_position() == other_organism.get_y_position() and (not self.get_collided_flag() and not other_organism.get_collided_flag()):
                    if other_organism.get_name() == "turtle" or other_organism.get_name() == "antelope" or other_organism.get_name() == "guarana" or other_organism.get_name() == "human" or other_organism.get_name() == "hogweed":
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
            organisms_copy.remove(self)
            self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        else:
            self.compareInitiatives(other_organism, organisms_copy)

    def compareInitiatives(self, other_organism, organisms_copy):
        if self.get_initiative() > other_organism.get_initiative():
            organisms_copy.remove(self)
            self.__game.appendMessage(f"<{self.get_name()}> died of {other_organism.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        elif self.get_initiative() < other_organism.get_initiative():
            organisms_copy.remove(other_organism)
            self.__game.appendMessage(f"<{other_organism.get_name()}> died of {self.get_name()}")
            self.set_collided_flag(True)
            other_organism.set_collided_flag(True)
        else:
            self.spreadAnimals(other_organism, organisms_copy)

    def spreadAnimals(self, other_organism, organisms_copy):
        if not self.get_collided_flag() and not other_organism.get_collided_flag() and not self.get_is_plant_flag() and not other_organism.get_is_plant_flag():
            a = [self.get_x_position()]
            b = [self.get_y_position()]
            self.generateRandomCoordinates(a, b)
            a_int = a[0]
            b_int = b[0]
            new_organism = self.createInstanceOfOrganism(self.__game, self.__size)

            if new_organism is not None:
                new_organism.set_x_position(a_int)
                new_organism.set_y_position(b_int)
                new_organism.set_age(1)
                new_organism.set_collided_flag(True)
                new_organism.set_index(len(organisms_copy))
                self.draw(a_int, b_int, self.__size.get_ratio())
                organisms_copy.append(new_organism)

                self.__game.appendMessage(f"<simulation> two animals of type {self.get_name()} have multiplied")
                self.set_collided_flag(True)
                other_organism.set_collided_flag(True)

    def draw(self, x, y, animal_size):
        x_position = x
        y_position = y
        animal_width = x + animal_size
        animal_height = y + animal_size

        self.__game.get_canvas().create_rectangle(x_position, y_position, animal_width, animal_height,
                                                  fill=self.get_color())
        self.__game.appendMessage(f"<{self.get_name()}> coords: ({x_position // self.__size.get_ratio()}, "
                                  f"{y_position // self.__size.get_ratio()})")

    # pure virtual functions:

    @abstractmethod
    def createInstanceOfOrganism(self, game, size):
        pass

    @abstractmethod
    def action(self, x, y, organisms_copy):
        pass

    # setters and getters:

    def set_power(self, power):
        self.__power = power

    def set_initiative(self, init):
        self.__initiative = init

    def set_name(self, name):
        self.__name = name

    def get_x_position(self):
        return self.__x_position

    def get_y_position(self):
        return self.__y_position

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_prev_x_position(self, x):
        self.__x_position_prev = x

    def set_prev_y_position(self, y):
        self.__y_position_prev = y

    def set_x_position(self, x):
        self.__x_position = x

    def set_y_position(self, y):
        self.__y_position = y

    def set_age(self, age):
        self.__age = age

    def set_index(self, index):
        self.__index.append(index)

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def get_power(self):
        return self.__power

    def get_initiative(self):
        return self.__initiative

    def get_index(self):
        return self.__index

    def set_collided_flag(self, value):
        self.__collided_flag = value

    def get_collided_flag(self):
        return self.__collided_flag

    def get_prev_x_position(self):
        return self.__x_position_prev

    def get_prev_y_position(self):
        return self.__y_position_prev

    def set_is_plant_flag(self, value):
        self.__is_plant_flag = value

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key

    def get_ability_flag(self):
        return self.__ability_flag

    def set_ability_flag(self, value):
        self.__ability_flag = value

    def get_timer(self):
        return self.__timer

    def set_timer(self, time):
        self.__timer = time

    def get_cool_down(self):
        return self.__cool_down

    def set_cool_down(self, value):
        self.__cool_down = value

    def get_is_plant_flag(self):
        return self.__is_plant_flag

