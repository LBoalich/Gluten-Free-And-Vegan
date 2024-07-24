import tkinter as tk
from tkinter import ttk

#Define category refine window
class CategoryWindow(ttk.Frame):
    '''Allows users to further refine filter based on the restaurant categories.'''
    def __init__(self, parent, controller):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller
        #Set up grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        #Create check buttons variable
        self.catCheckVar = tk.StringVar() #used to get the on/off value of the checkbutton
        #Initialize the instance variables for the data
        self.categories = self.controller.getCategoryList()
        ##Create and add category label
        self.categoryLabel = ttk.Label(self, text="Categories:")
        self.categoryLabel.grid(row=0, column=0)
        #Method to create and add category refinement
        def addCategory(self):
            row = 0
            column = 1
            for category in self.categories:
                ttk.Checkbutton(self, text=category, onvalue=category, variable=self.catCheckVar).grid(row=row, column=column, sticky="W")
                if column == 1:
                    column = 2
                else:
                    row += 1
                    column = 1
        addCategory(self)
