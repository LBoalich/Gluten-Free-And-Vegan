import tkinter as tk
from tkinter import ttk

#Define category refine window
class CategoryWindow(ttk.Frame):
    '''Allows users to further refine filter based on the restaurant categories.'''
    def __init__(self, parent, controller):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller
        #Initialize the instance variables for the data
        self.categories = self.controller.getCategoryList()
        #Create radiobutton variable attribute
        self.refineCategoryVar = tk.StringVar()
        #Set radiobutton default value to vegan
        self.refineCategoryVar.set("Vegan")
        #Create list to hold the radio buttons
        self.refineCategoryRadiobuttons = []
        #Set up grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        ##Create and add category label
        self.categoryLabel = ttk.Label(self, text="Categories:")
        self.categoryLabel.grid(row=0, column=0)
    
        #Method to create and add category refinement
        def addCategory(self):
            row = 0
            column = 1
            for category in self.categories:     
                radiobutton = tk.Radiobutton(self, text=category, variable=self.refineCategoryVar, value=category)
                self.refineCategoryRadiobuttons.append(radiobutton)
                radiobutton.grid(row=row, column=column, sticky="W")

                if column == 1:
                    column = 2
                else:
                    row += 1
                    column = 1

        addCategory(self)