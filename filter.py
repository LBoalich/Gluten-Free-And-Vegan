#Imports
import tkinter as tk
from tkinter import ttk

#Define filter window class
class FilterWindow(ttk.Frame):
    """Allows users to filter by selecting from the following categories: hours, category, neighborhood, entree price range, happy hour & specials."""
    def __init__(self, parent, controller):
        """Sets up window and widgets."""
        super().__init__(parent)
        #Set up grid
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)
        #Create and add filter label to the window
        self.filterLabel = ttk.Label(self, text="Filter Categories")
        self.filterLabel.grid(row=0, column=0)
        #Create check buttons
        checkVar = tk.StringVar() #used to get the on/off value of the checkbutton
        self.hoursCheck = tk.Checkbutton(self, text="Hours", onvalue="Hours", variable=checkVar)
        self.categoryCheck = tk.Checkbutton(self, text="Category", onvalue="Category", variable=checkVar)
        self.neighborhoodCheck = tk.Checkbutton(self, text="Neighborhood", onvalue="Neighborhood", variable=checkVar)
        self.entreeCheck = tk.Checkbutton(self, text="Entree Price Range", onvalue="Entree Price Range", variable=checkVar)
        self.happyHourCheck = tk.Checkbutton(self, text="Happy Hour & Specials", onvalue="Happy Hour & Specials", variable=checkVar)
        #Add check buttons
        self.hoursCheck.grid(row=1, column=0, sticky="W")
        self.categoryCheck.grid(row=2, column=0, sticky="W")
        self.neighborhoodCheck.grid(row=3, column=0, sticky="W")
        self.entreeCheck.grid(row=4, column=0, sticky="W")
        self.happyHourCheck.grid(row=5, column=0, sticky="W")
        #Create and add filter button
        self.filterButton = ttk.Button(self, text="Filter", command=lambda :controller.setWindow("RefineWindow"))
        self.filterButton.grid(row=6, column=0)     
