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
        #Create checkbutton  and variable dictionary 
        self.categoryVarDictionary = {}
        self.categoryCheckbuttonDictionary = {}
        #Populate the dictionaires
        for category in self.categories:
            self.categoryVarDictionary[category] = tk.IntVar()
            self.categoryCheckbuttonDictionary[category] = "checkbutton"
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
            for key in self.categoryVarDictionary:     
                checkbutton = ttk.Checkbutton(
                    self, 
                    text=key, 
                    onvalue=1, 
                    offvalue=0, 
                    variable=self.categoryVarDictionary[key],
                    command=lambda: [
                        self.controller.setRefineCategoryVar(category,
                        self.categoryVarDictionary[key].get()), print(self.categoryVarDictionary[category].get()), 
                        print(self.categoryVarDictionary.items())])
                self.categoryCheckbuttonDictionary[category] = checkbutton
                self.categoryCheckbuttonDictionary[category].grid(row=row, column=column, sticky="W")
                
                if column == 1:
                    column = 2
                else:
                    row += 1
                    column = 1

        addCategory(self)
