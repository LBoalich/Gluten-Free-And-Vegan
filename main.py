"""
Name: Gluten Free and Vegan
Author: Leah Boalich
Date: 07/15/24
Assignment: Final Project
Short Description: This program allows users to search for restaurants in the Charlotte, NC region that serve gluten free options that are also vegan or vegetarian.  Users can also use a filter to find matching restaurants.  
"""

#Imports
import tkinter as tk
from tkinter import ttk 
from restaurantList import restaurantList
from controller import Controller

#Define main class to run the program
class Main(tk.Tk):
    """Allows users to search for restaurants using search or filter."""
    def __init__(self):
        """Sets up the main window and widgets and data."""
        super().__init__()
        self.title("GLUTEN FREE AND VEGAN")
        self.geometry("1000x700")
        self.mainWindow = ttk.Frame(self)
        self.mainWindow.pack(side="top", fill="both", expand = True)
        self.mainWindow.grid_rowconfigure(0, weight=1)
        self.mainWindow.grid_columnconfigure(0, weight=1)
        #Initialize the controller
        Controller(self.mainWindow, restaurantList)
        #Run the program
        self.mainloop()

#Automatically run program
if __name__ == "__main__":
    Main()
