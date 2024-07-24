import tkinter as tk
from tkinter import ttk

#Define specials window class
class SpecialsWindow(ttk.Frame):
    """Allows user to find restaurants that have happy hours or specails."""
    def __init__(self, parent, controller):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller
        #Set up grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #Create and add specials checkbutton
        self.specialCheck = tk.IntVar()
        self.specialsCheckbutton = tk.Checkbutton(self, text="Has Happy Hour or Specials", variable=self.specialCheck)
        self.specialsCheckbutton.grid(row=0, column=0)
