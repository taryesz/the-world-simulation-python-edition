import tkinter as tk
import traceback
from tkinter import messagebox
from tkinter import scrolledtext
from sprites.animals.Wolf import Wolf
from sprites.animals.Sheep import Sheep
from sprites.animals.Fox import Fox
from sprites.animals.Antelope import Antelope
from sprites.animals.Turtle import Turtle
from sprites.plants.Grass import Grass
from sprites.plants.Dandelion import Dandelion
from sprites.plants.Guarana import Guarana
from sprites.plants.Nightshade import Nightshade
from sprites.plants.Hogweed import Hogweed
from sprites.animals.Human import Human
from sprites.animals.Cyber import Cyber


class Game:

    def __init__(self, size):
        self.__choose_window_height = 350
        self.__choose_window_width = 300
        self.__choose = None
        self.__var = None
        self.__chose_window_open_flag = False
        self.__max_time = 10
        self.__message_frame = None
        self.__organisms_copy = []
        self.__message_area = None
        self.__message_window_height = 500
        self.__message_window_width = 400
        self.__root = None
        self.__canvas = None
        self.__size = size
        self.__window_open = False
        self.__organisms = []
        self.__animal_size = self.__size.get_ratio()

    def createGameObject(self):
        self.createMessageWindow()
        self.createOrganisms()
        self.createWindow()
        self.drawOrganisms()
        self.bindArrowKeys()
        return

    def createWindow(self):
        if not self.__window_open:
            width = self.__size.get_board_width()
            height = self.__size.get_board_height()

            self.__root = tk.Tk()
            self.__root.title("The World Simulation")
            self.__root.geometry(f"{width}x{height}")
            self.__root.resizable(False, False)
            self.__root.protocol("WM_DELETE_WINDOW", self.onWindowClose)
            self.__window_open = True

            self.__canvas = tk.Canvas(self.__root, width=width, height=height)
            self.__canvas.pack()

        else:
            messagebox.showwarning("Starting new game",
                                   "Loading new game...")

            self.__canvas.delete("all")
            self.__root.destroy()
            self.__message_frame.destroy()
            self.__window_open = False
            self.__organisms = []
            self.__organisms_copy = []
            self.createGameObject()

    def onWindowClose(self):
        self.__window_open = False
        self.__root.destroy()

    def createOrganisms(self):
        index = [0]
        human = True

        fox = Fox(self, self.__size)
        fox.initializeOrganisms(fox, index, not human)

        wolf = Wolf(self, self.__size)
        wolf.initializeOrganisms(wolf, index, not human)

        human_object = Human(self, self.__size)
        human_object.initializeOrganisms(human_object, index, human)

        sheep = Sheep(self, self.__size)
        sheep.initializeOrganisms(sheep, index, not human)

        antelope = Antelope(self, self.__size)
        antelope.initializeOrganisms(antelope, index, not human)

        cyber = Cyber(self, self.__size)
        cyber.initializeOrganisms(cyber, index, not human)

        turtle = Turtle(self, self.__size)
        turtle.initializeOrganisms(turtle, index, not human)

        grass = Grass(self, self.__size)
        grass.initializeOrganisms(grass, index, not human)

        dandelion = Dandelion(self, self.__size)
        dandelion.initializeOrganisms(dandelion, index, not human)

        guarana = Guarana(self, self.__size)
        guarana.initializeOrganisms(guarana, index, not human)

        nightshade = Nightshade(self, self.__size)
        nightshade.initializeOrganisms(nightshade, index, not human)

        hogweed = Hogweed(self, self.__size)
        hogweed.initializeOrganisms(hogweed, index, not human)

    def drawOrganisms(self):
        for organism in self.__organisms:
            x = organism.get_x_position()
            y = organism.get_y_position()
            organism.draw(x, y, self.__animal_size)

    def createMessageWindow(self):
        if not self.__window_open:
            self.__message_frame = tk.Tk()
            self.__message_frame.title("Messages")
            self.__message_frame.geometry(f"{self.__message_window_width}x{self.__message_window_height}")
            self.__message_frame.resizable(False, False)
            self.__message_frame.protocol("WM_DELETE_WINDOW", self.__message_frame.iconify)

            self.__message_area = scrolledtext.ScrolledText(self.__message_frame, wrap=tk.WORD)
            self.__message_area.configure(state='disabled')
            self.__message_area.pack(fill=tk.BOTH, expand=True)

    def onChooseWindowClose(self):
        self.__root.destroy()

    def createChooseWindow(self, x, y):
        width = self.__choose_window_width
        height = self.__choose_window_height

        self.__choose = tk.Tk()
        self.__choose.title("Choose a creature to create")
        self.__choose.geometry(f"{width}x{height}")
        self.__choose.resizable(False, False)
        self.__choose.protocol("WM_DELETE_WINDOW", self.onChooseWindowClose)

        wolf_button = tk.Button(self.__choose, text="Wolf", command=lambda: self.addOrganism("wolf", x, y))
        wolf_button.pack(anchor=tk.W)

        sheep_button = tk.Button(self.__choose, text="Sheep", command=lambda: self.addOrganism("sheep", x, y))
        sheep_button.pack(anchor=tk.W)

        fox_button = tk.Button(self.__choose, text="Fox", command=lambda: self.addOrganism("fox", x, y))
        fox_button.pack(anchor=tk.W)

        turtle_button = tk.Button(self.__choose, text="Turtle", command=lambda: self.addOrganism("turtle", x, y))
        turtle_button.pack(anchor=tk.W)

        antelope_button = tk.Button(self.__choose, text="Antelope", command=lambda: self.addOrganism("antelope", x, y))
        antelope_button.pack(anchor=tk.W)

        cyber_button = tk.Button(self.__choose, text="Cyber Sheep", command=lambda: self.addOrganism("cyber", x, y))
        cyber_button.pack(anchor=tk.W)

        grass_button = tk.Button(self.__choose, text="Grass", command=lambda: self.addOrganism("grass", x, y))
        grass_button.pack(anchor=tk.W)

        dandelion_button = tk.Button(self.__choose, text="Dandelion", command=lambda: self.addOrganism("dandelion", x, y))
        dandelion_button.pack(anchor=tk.W)

        guarana_button = tk.Button(self.__choose, text="Guarana", command=lambda: self.addOrganism("guarana", x, y))
        guarana_button.pack(anchor=tk.W)

        nightshade_button = tk.Button(self.__choose, text="Nightshade", command=lambda: self.addOrganism("nightshade", x, y))
        nightshade_button.pack(anchor=tk.W)

        hogweed_button = tk.Button(self.__choose, text="Hogweed", command=lambda: self.addOrganism("hogweed", x, y))
        hogweed_button.pack(anchor=tk.W)

    def addOrganism(self, name, x, y):
        new_organism = self.spawn(name)

        if new_organism is not None:
            new_organism.set_x_position(x)
            new_organism.set_y_position(y)
            new_organism.set_age(1)
            new_organism.set_index(len(self.__organisms)+1)
            new_organism.draw(x, y, self.__size.get_ratio())
            self.appendMessage(f"<simulation> added organism of type {new_organism.get_name()}")
            self.addOrganismToOrganismsList(new_organism)

        self.__chose_window_open_flag = False
        self.__choose.destroy()

    def appendMessage(self, text):
        self.__message_area.configure(state='normal')
        self.__message_area.insert(tk.END, f"{text}.\n")
        self.__message_area.configure(state='disabled')

    def bindArrowKeys(self):
        self.__root.bind('<Up>', lambda event: self.keyPressed("<Up>"))
        self.__root.bind('<Down>', lambda event: self.keyPressed("<Down>"))
        self.__root.bind('<Left>', lambda event: self.keyPressed("<Left>"))
        self.__root.bind('<Right>', lambda event: self.keyPressed("<Right>"))
        self.__root.bind('<space>', lambda event: self.keyPressed("<Space>"))
        self.__root.bind('s', lambda event: self.keyPressed("<S>"))
        self.__root.bind('l', lambda event: self.keyPressed("<L>"))
        self.__canvas.bind("<ButtonPress>", self.mousePressed)

    def mousePressed(self, event):
        if event.num == 1:
            x = event.x
            y = event.y
            new_x = x
            new_y = y

            new_x = self.findNearestCoordinate(x)
            new_y = self.findNearestCoordinate(y)

            if not self.__chose_window_open_flag:
                self.__chose_window_open_flag = True
                self.createChooseWindow(new_x, new_y)
            else:
                messagebox.showwarning("Window Already Open", "The spawn-creature window is already open.")

    def findNearestCoordinate(self, coordinate):
        if coordinate % self.__size.get_ratio() == 0:
            return coordinate
        else:
            lowerCoordinate = (coordinate // self.__size.get_ratio()) * self.__size.get_ratio()
            upperCoordinate = lowerCoordinate + self.__size.get_ratio()
            lowerDistance = abs(coordinate - lowerCoordinate)
            upperDistance = abs(coordinate - upperCoordinate)

            return lowerCoordinate if lowerDistance < upperDistance else upperCoordinate

    def keyPressed(self, key_code):
        if key_code == "<Up>" or key_code == "<Down>" or key_code == "<Left>" or key_code == "<Right>":
            for organism in self.__organisms:
                if key_code == "<Up>":
                    organism.set_key("up")
                elif key_code == "<Down>":
                    organism.set_key("down")
                elif key_code == "<Left>":
                    organism.set_key("left")
                elif key_code == "<Right>":
                    organism.set_key("right")

                if organism.get_cool_down():
                    timer = organism.get_timer()
                    timer += 1
                    organism.set_timer(timer)
                    if organism.get_timer() == self.__max_time:
                        organism.set_timer(0)
                        organism.set_cool_down(False)
                        organism.set_ability_flag(False)
                        self.appendMessage("<player> ability cooldown ended")
                else:
                    if organism.get_ability_flag():
                        self.appendMessage("<player> using ability..")
                        organism.set_cool_down(True)
                        organism.set_timer(0)

            self.performAction()
        elif key_code == "<Space>":
            human_found_flag = False
            for organism in self.__organisms:
                if organism.get_name() == "human":
                    human_found_flag = True
                    if organism.get_cool_down():
                        self.appendMessage("<human> cooldown, cannot use ability")
                    else:
                        self.appendMessage("<human> ability activated for 5 turns")
                        organism.set_ability_flag(True)
                        organism.set_timer(0)
                        organism.set_cool_down(True)
                    break
        elif key_code == "<S>":
            self.saveGame()
        elif key_code == "<L>":
            self.loadGame()

    def performAction(self):

        self.__canvas.delete("all")
        self.__organisms_copy = []

        for organism in self.__organisms:
            age = organism.get_age()
            age += 1
            organism.set_age(age)
            organism.set_prev_x_position(organism.get_x_position())
            organism.set_prev_y_position(organism.get_y_position())
            x_position = []
            y_position = []
            x_position.append(organism.get_x_position())
            y_position.append(organism.get_y_position())
            organism.action(x_position, y_position, self.__organisms_copy)
            organism.set_x_position(x_position[0])
            organism.set_y_position(y_position[0])
            self.__organisms_copy.append(organism)

        for organism in self.__organisms:
            organism.collide(self.__organisms_copy)
            organism.set_collided_flag(False)

        self.__organisms = self.__organisms_copy
        self.sortOrganisms(self.__organisms)

    def sortOrganisms(self, organisms):
        number_of_organisms = len(organisms)
        swapped = True

        while swapped:
            swapped = False

            for i in range(number_of_organisms - 1):

                if organisms[i].get_initiative() < organisms[i + 1].get_initiative():
                    organisms[i], organisms[i + 1] = organisms[i + 1], organisms[i]
                    swapped = True

                elif organisms[i].get_initiative() == organisms[i + 1].get_initiative():

                    if organisms[i].get_age() < organisms[i + 1].get_age():
                        organisms[i], organisms[i + 1] = organisms[i + 1], organisms[i]
                        swapped = True

            number_of_organisms -= 1

    def addOrganismToOrganismsList(self, organism):
        self.__organisms.append(organism)

    def saveGame(self):
        try:
            with open("saved.txt", "w") as writer, open("world.txt", "w") as worldWriter:
                worldWidth = self.__size.get_board_width()
                worldHeight = self.__size.get_board_height()
                worldWriter.write(str(worldWidth) + " " + str(worldHeight) + '\n')
                for org in self.__organisms:
                    x = org.get_x_position()
                    y = org.get_y_position()
                    age = org.get_age()
                    idx = org.get_index()
                    if len(idx) > 0 and idx[0] is not None:
                        name = org.get_name()
                        writer.write(name + " " + str(idx[0]) + " " + str(age) + " " + str(x) + " " + str(y) + '\n')
            self.appendMessage("<simulation> saved game to file")
        except IOError:
            self.appendMessage("<simulation> an error occurred while trying to save the game to file")
            traceback.print_exc()

    def loadGame(self):
        self.__organisms = []
        try:
            with open("world.txt", "r") as worldReader:
                world = worldReader.readline()
                if world is not None:
                    sizes = world.split(" ")
                    worldWidth = int(sizes[0])
                    worldHeight = int(sizes[1])
                    self.__size.set_board_width(worldWidth)
                    self.__size.set_board_height(worldHeight)

            with open("saved.txt", "r") as reader:
                line = reader.readline()

                while line:
                    parts = line.split(" ")
                    name = parts[0]
                    idx = int(parts[1])
                    age = int(parts[2])
                    x = int(parts[3])
                    y = int(parts[4])

                    new_organism = self.spawn(name)

                    if new_organism is not None:
                        new_organism.set_x_position(x)
                        new_organism.set_y_position(y)
                        new_organism.set_age(age)
                        new_organism.set_index(idx)
                        new_organism.draw(x, y, self.__size.get_ratio())
                        self.addOrganismToOrganismsList(new_organism)

                    line = reader.readline()
            self.__canvas.delete("all")
            self.__root.destroy()
            self.__message_frame.destroy()
            self.__window_open = False
            self.createMessageWindow()
            self.createWindow()
            self.drawOrganisms()
            self.bindArrowKeys()
        except IOError as e:
            traceback.print_exc()

    def spawn(self, name):
        if name == "wolf":
            return Wolf(self, self.__size)
        elif name == "sheep":
            return Sheep(self, self.__size)
        elif name == "fox":
            return Fox(self, self.__size)
        elif name == "turtle":
            return Turtle(self, self.__size)
        elif name == "antelope":
            return Antelope(self, self.__size)
        elif name == "cyber":
            return Cyber(self, self.__size)
        elif name == "grass":
            return Grass(self, self.__size)
        elif name == "dandelion":
            return Dandelion(self, self.__size)
        elif name == "guarana":
            return Guarana(self, self.__size)
        elif name == "nightshade":
            return Nightshade(self, self.__size)
        elif name == "hogweed":
            return Hogweed(self, self.__size)
        elif name == "human":
            return Human(self, self.__size)

    # getters:

    def get_organisms_copy(self):
        return self.__organisms_copy

    def get_organisms(self):
        return self.__organisms

    def get_canvas(self):
        return self.__canvas
