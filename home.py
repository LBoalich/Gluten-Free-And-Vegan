import tkinter as tk
from tkinter import ttk
from search import SearchWindow
from filter import FilterWindow

#Define home page
class HomePage(ttk.Frame):
    """Allows user to find a restaurant using search or filter."""
    def __init__(self, parent, controller):
        """Sets up the window using search window and filter window classes."""
        super().__init__(parent)
        self.controller = controller #Create the controller
        #Set up grid
        self.pack(side="top", fill="both", expand = True)
        self.grid_rowconfigure((0,2), weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_columnconfigure(0, weight=1)
        #Creates search window frame
        self.searchWindow = SearchWindow(self, self.controller) 
        #Creates filter window frame
        self.filterWindow = FilterWindow(self, self.controller) 
        #Create exit button
        self.exitButton = ttk.Button(self, text="Exit Program", command=parent.quit)
        #Add search window to homepage frame
        self.searchWindow.grid(row=0, column=0) 
        #Add filter window to homepage frame
        self.filterWindow.grid(row=1, column=0) 
        #Add exit button to homepage frame
        self.exitButton.grid(row=2, column=0)