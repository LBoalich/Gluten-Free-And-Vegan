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
        #Create widgets
        self.searchWindow = SearchWindow(self)
        self.filterWindow = FilterWindow(self, controller)
        #Add widgets
        self.searchWindow.pack()
        self.filterWindow.pack()
