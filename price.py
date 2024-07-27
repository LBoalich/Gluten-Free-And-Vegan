import tkinter as tk
from tkinter import ttk

#Define entree price range refine window
class PriceWindow(ttk.Frame):
    """Allows users to filter the price range of an entree"""
    def __init__(self, parent, controller):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller #Create controller
        #Set up grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        #Create price scales
        self.lowScale = tk.Scale(self, from_=5, to =200, orient="horizontal", label="Low Entree Price:", length=200) 
        self.highScale = tk.Scale(self, from_=5, to =200, orient="horizontal", label="High Entree Price:", length=200)
        #Set high scale initial value to 200
        self.highScale.set(200)
        #Add price scales 
        self.lowScale.grid(row=0, column=0)
        self.highScale.grid(row=0, column=1)
