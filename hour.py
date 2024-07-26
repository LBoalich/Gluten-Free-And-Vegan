#Imports
import tkinter as tk
from tkinter import ttk

#Define hour refine window
class HourWindow(ttk.Frame):
    """Allows users to filter which hours the restaurant should be open"""
    def __init__(self, parent, controller):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller
        #Set up grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1), weight=1)
        #Create hour scales
        self.startScale = tk.Scale(self, from_=0, to =24, orient="horizontal", label="Open From:", length=200) 
        self.endScale = tk.Scale(self, from_=0, to =24, orient="horizontal", label="Open To:", length=200) 
        #Set end scale initial value to 24
        self.endScale.set(24)
        #Add hour scales
        self.startScale.grid(row=0, column=0)
        self.endScale.grid(row=0, column=1)
