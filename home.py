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
        self.controller = controller
        #Set up grid
        self.pack(side="top", fill="both", expand = True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_columnconfigure(0, weight=1)
        #Create widgets
        self.searchWindow = SearchWindow(self)
        self.filterWindow = FilterWindow(self, controller)
        #Add widgets
        self.searchWindow.grid(row=0, column=0)
        self.filterWindow.grid(row=1, column=0)
