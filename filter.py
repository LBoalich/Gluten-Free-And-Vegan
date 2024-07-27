#Imports
import tkinter as tk
from tkinter import ttk

#Define filter window class
class FilterWindow(ttk.Frame):
    """Allows users to filter by selecting from the following categories: hours, category, neighborhood, entree price range, happy hour & specials."""
    def __init__(self, parent, controller):
        """Sets up window and widgets."""
        super().__init__(parent)
        self.controller = controller #Create the controller
        #Set up grid
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)
        #Create and add filter label to the window
        self.filterLabel = ttk.Label(self, text="Filter Categories")
        self.filterLabel.grid(row=0, column=0)
        #Create checkbutton variables to get the on/off value of the  corresponding checkbutton
        self.hoursVar = tk.IntVar() 
        self.categoryVar = tk.IntVar() 
        self.neighborhoodVar = tk.IntVar() 
        self.entreeVar = tk.IntVar() 
        self.happyHourVar = tk.IntVar() 
        #Create the checkbuttons
        self.hoursCheck = ttk.Checkbutton(self, text="Hours", variable=self.hoursVar, onvalue=1, offvalue=0, command=lambda : self.controller.setHoursVar(self.hoursVar.get()))
        self.categoryCheck = ttk.Checkbutton(self, text="Category", variable=self.categoryVar, onvalue=1, offvalue=0, command=lambda : self.controller.setCategoryVar(self.categoryVar.get()))
        self.neighborhoodCheck = ttk.Checkbutton(self, text="Neighborhood", variable=self.neighborhoodVar, onvalue=1, offvalue=0, command=lambda : self.controller.setNeighborhoodVar(self.neighborhoodVar.get()))
        self.entreeCheck = ttk.Checkbutton(self, text="Entree Price Range", variable=self.entreeVar, onvalue=1, offvalue=0, command=lambda : self.controller.setPriceVar(self.entreeVar.get()))
        self.happyHourCheck = ttk.Checkbutton(self, text="Happy Hour & Specials", variable=self.happyHourVar, onvalue=1, offvalue=0, command=lambda : self.controller.setSpecialsVar(self.happyHourVar.get()))
        #Add checkbuttons
        self.hoursCheck.grid(row=1, column=0, sticky="W")
        self.categoryCheck.grid(row=2, column=0, sticky="W")
        self.neighborhoodCheck.grid(row=3, column=0, sticky="W")
        self.entreeCheck.grid(row=4, column=0, sticky="W")
        self.happyHourCheck.grid(row=5, column=0, sticky="W")
        #Create and add filter button
        self.filterButton = ttk.Button(self, text="Filter", command=lambda : [self.controller.setWindow("RefineWindow"), self.controller.addFilterCategoriesToRefine()])
        self.filterButton.grid(row=6, column=0)  
