import tkinter as tk
from tkinter import ttk

#Define neighborhood refine window
class NeighborhoodWindow(ttk.Frame):
    '''Allows users to further refine filter based on neighborhood.'''
    def __init__(self, parent):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        #Create check buttons variable
        hoodCheckVar = tk.StringVar() #used to get the on/off value of the checkbutton
        #Initialize the instance variables for the data
        self.hoods = ["hood1", "hood2", "hood3", "hood4", "hood5", "hood6", "hood7", "hood8", "hood9"]
        ##Create and add category label
        self.hoodLabel = ttk.Label(self, text="Neighborhoods:")
        self.hoodLabel.grid(row=0, column=0)
        #Method to create and add category refinement
        def addHoods(self):
            row = 0
            column = 1
            for hood in self.hoods:
                tk.Checkbutton(self, text=hood, onvalue=hood, variable=hoodCheckVar).grid(row=row, column=column, sticky="W")
                if column == 1:
                    column = 2
                else:
                    row += 1
                    column = 1

        addHoods(self)
