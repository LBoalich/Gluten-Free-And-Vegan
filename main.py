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

#Define search window class
class SearchWindow(ttk.Frame):
    """"Allows user to search for restaurants."""
    def __init__(self, parent):
        """Sets up window and widgets."""
        super().__init__(parent)
        #Create widgets
        self.searchLabel = ttk.Label(self, text="Restaurant Name:")
        self.searchEntry = ttk.Entry(self)
        self.searchButton = ttk.Button(self, text="Search")
        #Add widgets to window
        self.columnconfigure((0, 1, 2), weight=1, uniform=True)
        self.searchLabel.grid(row=0, column=0)
        self.searchEntry.grid(row=0, column=1)
        self.searchButton.grid(row=0, column=2)

#Define filter window class
class FilterWindow(ttk.Frame):
    """Allows users to filter by selecting from the following categories: hours, category, neighborhood, entree price range, happy hour & specials."""
    def __init__(self, parent):
        """Sets up window and widgets."""
        super().__init__(parent)
        #Create and add filter label to the window
        self.filterLabel = ttk.Label(self, text="Filter Categories")
        self.filterLabel.grid(row=0)
        #Create check buttons
        checkVar = tk.StringVar() #used to get the on/off value of the checkbutton
        self.hoursCheck = tk.Checkbutton(self, text="Hours", onvalue="Hours", variable=checkVar)
        self.categoryCheck = tk.Checkbutton(self, text="Category", onvalue="Category", variable=checkVar)
        self.neighborhoodCheck = tk.Checkbutton(self, text="Neighborhood", onvalue="Neighborhood", variable=checkVar)
        self.entreeCheck = tk.Checkbutton(self, text="Entree Price Range", onvalue="Entree Price Range", variable=checkVar)
        self.happyHourCheck = tk.Checkbutton(self, text="Happy Hour & Specials", onvalue="Happy Hour & Specials", variable=checkVar)
        #Add check buttons
        self.hoursCheck.grid(row=1, sticky="W")
        self.categoryCheck.grid(row=2, sticky="W")
        self.neighborhoodCheck.grid(row=3, sticky="W")
        self.entreeCheck.grid(row=4, sticky="W")
        self.happyHourCheck.grid(row=5, sticky="W")

#Define main class to run the program
class Main(tk.Tk):
    """Allows users to search for restaurants using search or filter."""
    def __init__(self):
        """Sets up the main window and widgets"""
        super().__init__()
        self.title("GLUTEN FREE AND VEGAN")
        self.minsize(700, 400)
        #Create widgets
        self.searchWindow = SearchWindow(self)
        self.filterWindow = FilterWindow(self)
        #Add widgets
        self.searchWindow.pack()
        self.filterWindow.pack()
        #Run the program
        self.mainloop()

#Automatically run program
if __name__ == "__main__":
    Main()