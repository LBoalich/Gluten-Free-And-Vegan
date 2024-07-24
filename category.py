import tkinter as tk
from tkinter import ttk

#Define category refine window
class CategoryWindow(ttk.Frame):
    '''Allows users to further refine filter based on the restaurant categories.'''
    def __init__(self, parent):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        #Set up grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        #Create check buttons variable
        catCheckVar = tk.StringVar() #used to get the on/off value of the checkbutton
        #Initialize the instance variables for the data
        self.categories = ["cat1", "cat2", "cat3", "cat4", "cat5", "cat6", "cat7", "cat8", "cat9"]
        ##Create and add category label
        self.categoryLabel = ttk.Label(self, text="Categories:")
        self.categoryLabel.grid(row=0, column=0)
        #Method to create and add category refinement
        def addCategory(self):
            row = 0
            column = 1
            for category in self.categories:
                tk.Checkbutton(self, text=category, onvalue=category, variable=catCheckVar).grid(row=row, column=column, sticky="W")
                if column == 1:
                    column = 2
                else:
                    row += 1
                    column = 1

        addCategory(self)
