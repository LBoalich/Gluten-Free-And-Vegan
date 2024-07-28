import tkinter as tk
from tkinter import ttk

#Define neighborhood refine window
class NeighborhoodWindow(ttk.Frame):
    '''Allows users to further refine filter based on neighborhood.'''
    def __init__(self, parent, controller):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller
        #Initialize the instance variables for the data
        self.hoods = self.controller.getNeighborhoodList()
        #Create attribute to hold the radiobutton variable
        self.refineNeighborhoodVar = tk.StringVar()
        #Set defualt value of radiobutton variable to "Noda"
        self.refineNeighborhoodVar.set("Noda")
        #Create list to hold the radiobuttons
        self.neighborhoodsRadiobuttons = []
        #Set up grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)   
        ##Create and add category label
        self.hoodLabel = ttk.Label(self, text="Neighborhoods:")
        self.hoodLabel.grid(row=0, column=0)
        self.createNeighborhoods()
        self.addNeighborhoods()
    #Method to create and add neighborhood refinement
    def createNeighborhoods(self):
        for neighborhood in self.hoods:
            radiobutton = tk.Radiobutton(self, text=neighborhood, variable=self.refineNeighborhoodVar, value=neighborhood)
            self.neighborhoodsRadiobuttons.append(radiobutton)
    #Modult to add neighborhoods to windwo
    def addNeighborhoods(self):
        row = 0
        column = 1
        for radiobutton in self.neighborhoodsRadiobuttons:
            radiobutton.grid(row=row, column=column, sticky="W")
            if column == 1:
                column = 2
            else:
                row += 1
                column = 1
