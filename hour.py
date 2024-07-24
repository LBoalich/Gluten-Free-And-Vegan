#Imports
import tkinter as tk
from tkinter import ttk

#Define hour refine window
class HourWindow(ttk.Frame):
    """Allows users to filter which hours the restaurant should be open"""
    def __init__(self, parent):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        #Initialize the slider variables
        self.startVar = tk.IntVar()
        self.endVar = tk.IntVar()
        #Create hour scales
        self.startScale = tk.Scale(self, variable = self.startVar, from_=1, to =24, orient="horizontal", label="Open From:", length=200) 
        self.endScale = tk.Scale(self, variable = self.endVar, from_=1, to =24, orient="horizontal", label="Open To:", length=200) 
        #Set end scale initial value to 24
        self.endScale.set(24)
        #Add hour scales
        self.startScale.grid(row=0, column=0)
        self.endScale.grid(row=0, column=1)
