#Imports
import tkinter as tk
from tkinter import ttk

#Define search window class
class SearchWindow(ttk.Frame):
    """"Allows user to search for restaurants."""
    def __init__(self, parent, controller):
        """Sets up window and widgets."""
        super().__init__(parent)
        self.controller = controller #Create the controller
        #Set up grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform=True)
        #Create widgets
        self.searchLabel = ttk.Label(self, text="Restaurant Name:") #Create search label
        self.searchEntry = ttk.Entry(self) #Create search entry 
        self.searchButton = ttk.Button(self, text="Search") #Create search button
        #Add widgets to window
        self.searchLabel.grid(row=0, column=0) #Add search label to search window
        self.searchEntry.grid(row=0, column=1)  #Add search entry to search window
        self.searchButton.grid(row=0, column=2) #Add search button to search window
