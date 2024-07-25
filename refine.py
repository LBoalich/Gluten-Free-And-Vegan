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
        self.controller = controller
        #Set up grid
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.grid_columnconfigure(0, weight=1)
        #Create and add further refine label
        self.refineLabel = ttk.Label(self, text="Refine Filter")
        self.refineLabel.grid(row=0, column=0)
        #Create the classes that allow refinement
        self.hourWindow = HourWindow(self, self.controller)
        self.categoryWindow = CategoryWindow(self, self.controller)
        self.neighborhoodWindow = NeighborhoodWindow(self, self.controller)
        self.priceWindow = PriceWindow(self, self.controller)
        self.specialsWindow = SpecialsWindow(self, self.controller)
        #Create and add filter button
        self.refineButton = ttk.Button(self, text="Refine Filter", command=lambda : self.controller.setWindow("ResultsWindow"))
        self.refineButton.grid(row=6, column=0)
