import tkinter as tk


class Type:

    def __init__(self):
        self.__board_type = None
        self.__hexagonal_button = None
        self.__square_button = None
        self.__root_size = 150
        self.__root_padding = 20
        self.__root = None

    def get_board_type(self):
        return self.__board_type

    def createTypeObject(self):
        self.createWindow()
        self.createButtons()
        self.adjustWindowSize()
        return

    def createWindow(self):
        self.__root = tk.Tk()
        self.__root.title("Choose the board type")

        self.__root.geometry(f"{self.__root_size}x{self.__root_size}")
        self.__root.resizable(False, False)

    def createButtons(self):

        frame_rel_x = 0.5
        frame_rel_y = 0.5

        frame = tk.Frame(self.__root)
        frame.place(relx=frame_rel_x, rely=frame_rel_y, anchor="center")

        button_width = 20

        row = 0
        column = 0
        button_pad_y = (0, self.__root_padding)

        self.__square_button = tk.Button(frame, text="Squared Board", width=button_width,
                                         command=self.selectSquaredBoard)
        self.__square_button.grid(row=row, column=column, pady=button_pad_y)

        row += 1
        button_pad_y = (0, self.__root_padding * 0.5)

        self.__hexagonal_button = tk.Button(frame, text="Hexagonal Board", width=button_width,
                                            command=self.selectHexagonalBoard)
        self.__hexagonal_button.grid(row=row, column=column, pady=button_pad_y)

    def adjustWindowSize(self):
        self.__root.update_idletasks()
        width = max(self.__square_button.winfo_reqwidth(),
                    self.__hexagonal_button.winfo_reqwidth()) + self.__root_padding * 2
        height = self.__root_size - self.__root_padding

        self.__root.geometry(f"{width}x{height}")

        self.__root.mainloop()

    def selectSquaredBoard(self):
        print("Squared Board selected")
        self.__board_type = "sq"
        self.__root.destroy()

    def selectHexagonalBoard(self):
        print("Hexagonal Board selected")
        self.__board_type = "hx"
        self.__root.destroy()
