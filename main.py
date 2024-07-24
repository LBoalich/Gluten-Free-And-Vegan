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
from refine import RefineWindow
from results import ResultsWindow
from home import HomePage      

#Define main class to run the program
class Main(tk.Tk):
    """Allows users to search for restaurants using search or filter."""
    def __init__(self):
        """Sets up the main window and widgets"""
        super().__init__()
        self.title("GLUTEN FREE AND VEGAN")
        self.geometry("700x400")
        self.mainWindow = ttk.Frame(self)
        self.mainWindow.pack(side="top", fill="both", expand = True)
        self.mainWindow.grid_rowconfigure(0, weight=1)
        self.mainWindow.grid_columnconfigure(0, weight=1)
        self.windows = {}
        #Fill the window dictionary
        for window in (HomePage, RefineWindow, ResultsWindow):
            windowName = window.__name__
            frame = window(self.mainWindow, controller=self)
            self.windows[windowName] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #Set the home page as the current window
        self.setWindow("HomePage")
        #Run the program
        self.mainloop()
    #Define module to set the current window shown
    def setWindow(self, window):
        currentWindow = self.windows[window]
        currentWindow.tkraise()

#Automatically run program
if __name__ == "__main__":
    Main()
