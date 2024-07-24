#Imports
import tkinter as tk
from tkinter import ttk
from hour import HourWindow
from category import CategoryWindow
from neighborhood import NeighborhoodWindow
from price import PriceWindow
from specials import SpecialsWindow

#Define refine filter window class
class RefineWindow(ttk.Frame):
    """Allows users to further refine the filter based on the categories picked in the filter window."""
    def __init__(self, parent, controller):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        #Create and add filter button
        self.refineButton = ttk.Button(self, text="Refine Filter", command=lambda : controller.setWindow("ResultsWindow"))
        self.refineButton.grid(row=0, column=1)
        #Create the classes that allow refinement
        self.hourWindow = HourWindow(self)
        self.categoryWindow = CategoryWindow(self)
        self.neighborhoodWindow = NeighborhoodWindow(self)
        self.priceWindow = PriceWindow(self)
        self.specialsWindow = SpecialsWindow(self)
        #Add the classes
        self.hourWindow.grid(row=2, column=0)
        self.categoryWindow.grid(row=3, column=0)
        self.neighborhoodWindow.grid(row=4, column=0)
        self.priceWindow.grid(row=5, column=0)
        self.specialsWindow.grid(row=6, column=0)
