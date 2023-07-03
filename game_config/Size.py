import tkinter as tk
from tkinter import messagebox


class Size:

    def __init__(self):
        self.__board_height = 400
        self.__board_width = 400  # size * 20 (ratio)
        self.__root_height = None
        self.__root_width = None
        self.__submit = None
        self.__height_label = None
        self.__width_label = None
        self.__input_board_height = None
        self.__input_board_width = None
        self.__root = None
        self.__root_padding = 20
        self.__spinbox_from = 10
        self.__spinbox_to = 35
        self.__ratio = 20

    def get_board_width(self):
        return self.__board_width

    def get_board_height(self):
        return self.__board_height

    def set_board_width(self, width):
        self.__board_width = width

    def set_board_height(self, height):
        self.__board_height = height

    def get_ratio(self):
        return self.__ratio

    def createSizeObject(self):
        self.createWindow()
        self.createButtons()
        self.adjustWindowSize()
        return

    def createWindow(self):
        self.__root = tk.Tk()
        self.__root.title("Choose the board size")

        width = self.__root_padding + self.__root_padding
        height = self.__root_padding + self.__root_padding

        self.__root_width = width
        self.__root_height = height

        self.__root.geometry(f"{self.__root_width}x{self.__root_height}")
        self.__root.resizable(False, False)

    def createButtons(self):
        row = 0
        column = 0

        self.__width_label = tk.Label(self.__root, text="Width:")
        self.__width_label.grid(row=row, column=column, padx=self.__root_padding, pady=self.__root_padding, sticky="w")

        self.__input_board_width = tk.Spinbox(self.__root, from_=self.__spinbox_from, to=self.__spinbox_to)
        self.__input_board_width.grid(row=row, column=column + 1,
                                      padx=self.__root_padding, pady=self.__root_padding,
                                      sticky="w")

        row += 1

        self.__height_label = tk.Label(self.__root, text="Height:")
        self.__height_label.grid(row=row, column=column, padx=self.__root_padding, pady=self.__root_padding, sticky="w")

        self.__input_board_height = tk.Spinbox(self.__root, from_=self.__spinbox_from, to=self.__spinbox_to)
        self.__input_board_height.grid(row=row, column=column + 1,
                                       padx=self.__root_padding, pady=self.__root_padding,
                                       sticky="w")

        row += 1

        self.__submit = tk.Button(self.__root, text="Submit", command=self.saveSizes)
        self.__submit.grid(row=row, column=column, columnspan=2, padx=self.__root_padding, pady=self.__root_padding)

    def adjustWindowSize(self):
        width = self.__width_label.winfo_reqwidth() + self.__input_board_width.winfo_reqwidth() +\
                self.__root_padding * 4
        height = self.__height_label.winfo_reqheight() + self.__input_board_height.winfo_reqheight() + self.__submit.\
            winfo_reqheight() + self.__root_padding * 6

        self.__root_width = width
        self.__root_height = height

        self.__root.geometry(f"{self.__root_width}x{self.__root_height}")

        self.__root.mainloop()

    def saveSizes(self):

        try:
            temp_width = int(self.__input_board_width.get())
            self.__board_width = temp_width * self.__ratio
            if self.__board_width < (self.__spinbox_from * self.__ratio) or \
                    self.__board_width > (self.__spinbox_to * self.__ratio):
                raise ValueError(f"Width must be between {self.__spinbox_from} and {self.__spinbox_to}")
        except ValueError:
            messagebox.showerror("Error",
                                 f"Invalid input. Please enter an integer value between "
                                 f"{self.__spinbox_from} and {self.__spinbox_to} for width.")
            return

        try:
            temp_height = int(self.__input_board_height.get())
            self.__board_height = temp_height * self.__ratio
            if self.__board_height < (self.__spinbox_from * self.__ratio) or \
                    self.__board_height > (self.__spinbox_to * self.__ratio):
                raise ValueError(f"Height must be between {self.__spinbox_from} and {self.__spinbox_to}")
        except ValueError:
            messagebox.showerror("Error",
                                 f"Invalid input. Please enter an integer value between "
                                 f"{self.__spinbox_from} and {self.__spinbox_to} for width.")
            return

        print(self.__board_width)
        print(self.__board_height)

        self.__root.destroy()
