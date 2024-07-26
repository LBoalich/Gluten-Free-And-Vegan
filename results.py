import tkinter as tk
from tkinter import ttk
from resultsCheckbuttons import ResultsCheckbuttonsWindow

#Define filter results window class
class ResultsWindow(ttk.Frame):
    """Allows user to see results from filter and choose a restaurant to get more information"""
    def __init__(self, parent, controller):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller
        #Set up grid
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(0, weight=1) 
        #Create and add the label widget
        self.resultsLabel = ttk.Label(self, text="Results")
        self.resultsLabel.grid(row=0, column=0)
        #Create and add checkbuttons winodw
        self.resultsCheckbuttons = ResultsCheckbuttonsWindow(self, self.controller)
        self.resultsCheckbuttons.grid(row=1, column=0)  
        #Create and add see more info button
        self.infoButton = ttk.Button(self, text="See More Info", command=lambda :infoCommand(self))
        self.infoButton.grid(row=2, column=0)
        #Create command method for info button
        def infoCommand(self):
            return
