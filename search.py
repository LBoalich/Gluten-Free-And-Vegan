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
        #Create attribute to hold the combobox variable
        self.searchComboBoxVar = tk.StringVar()
        #Set up grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform=True)
        #Create search label
        self.searchLabel = ttk.Label(self, text="Restaurant Name:") 
        #Create search combobox
        self.searchComboBox = ttk.Combobox(self, textvariable=self.searchComboBoxVar)
        #Add value to the combobox
        self.searchComboBox["values"] = self.controller.restaurants.getNames()
        #Set default combobox value to the first option
        self.searchComboBox.current(0)
        #Create search button
        self.searchButton = ttk.Button(self, text="Search", command=lambda: self.controller.openResultWindow(self.controller.restaurants.nameMatch(self.searchComboBoxVar.get())))
        #Add widgets to window
        self.searchLabel.grid(row=0, column=0) #Add search label to search window
        self.searchComboBox.grid(row=0, column=1)  #Add search entry to search window
        self.searchButton.grid(row=0, column=2) #Add search button to search window
