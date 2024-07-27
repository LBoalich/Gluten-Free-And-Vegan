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
        #Create check buttons variable dictionay
        self.neighborhoodsCheckbuttonVariables = {}
        for neighborhood in self.hoods:
            self.neighborhoodsCheckbuttonVariables[neighborhood] = tk.StringVar()
        #Create dictionary to hold the checkbuttons
        self.neighborhoodsCheckbuttons = {}
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
        for neighborhood, variable in self.neighborhoodsCheckbuttonVariables.items():
            checkbutton = ttk.Checkbutton(self, text=neighborhood, onvalue=neighborhood, offvalue="Off", variable=variable, command=lambda: [print(self.neighborhoodsCheckbuttonVariables[neighborhood].get()), self.controller.setRefineNeighborhoodVar(neighborhood, self.neighborhoodsCheckbuttonVariables[neighborhood])])
            self.neighborhoodsCheckbuttons[neighborhood] = checkbutton
    #Modult to add neighborhoods to windwo
    def addNeighborhoods(self):
        row = 0
        column = 1
        for checkbutton in self.neighborhoodsCheckbuttons.values():
            checkbutton.grid(row=row, column=column, sticky="W")
            if column == 1:
                column = 2
            else:
                row += 1
                column = 1
