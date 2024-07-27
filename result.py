#Imports
import tkinter as tk
from tkinter import ttk

#Define filter window class
class ResultWindow(tk.Toplevel):
    """Allows users to view the restaurant information that they picked in results window."""
    def __init__(self, controller):
        """Sets up window, widgets and data."""
        tk.Toplevel.__init__(self)
        self.controller = controller
        #Create attribute to hold the selected restaurant
        self.restaurant = self.controller.getSelectedRestaurant()
        #Set up grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #Create and add restaurant information label
        self.restaurantLabel = ttk.Label(self, text=self.restaurant)
        self.restaurantLabel.grid(row=0, column=0)
