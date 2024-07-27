import tkinter as tk
from tkinter import ttk
from resultsRadiobuttons import ResultsRadiobuttonsWindow

#Define filter results window class
class ResultsWindow(ttk.Frame):
    """Allows user to see results from filter and choose a restaurant to get more information"""
    def __init__(self, parent, controller):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller #Create controller
        #Set up grid
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=1) 
        #Create and add the label widget
        self.resultsLabel = ttk.Label(self, text="Results")
        self.resultsLabel.grid(row=0, column=0)
        #Create and add checkbuttons winodw
        self.resultsRadiobuttons = ResultsRadiobuttonsWindow(self, self.controller)
        self.resultsRadiobuttons.grid(row=1, column=0) 
        #Create add no results label
        self.noResultsLabel = ttk.Label(self, text="No Results") 
        self.noResultsLabel.grid(row=1, column=0)
        #Create and add see more info button
        self.infoButton = ttk.Button(self, text="See More Info", command=lambda :[self.controller.setResultRadioVar(self.resultsRadiobuttons.resultVar.get()), self.controller.openResultWindow(self.controller.getSelectedRestaurant())])
        self.infoButton.grid(row=2, column=0)
