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

#Define refine filter window class
class RefineWindow(ttk.Frame):
    """Allows users to further refine the filter based on the categories picked in the filter window."""
    def __init__(self, parent):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        #Initialize the instance variables for the data
        self.NEIGHBORHOODS = ["hood1", "hood2", "hood3"]
        self.PRICE_RANGE = (5, 100)
        #Create label widget
        self.refineLabel = ttk.Label(self, text="Further Refine")
        #Add label widgets
        self.refineLabel.grid(row=0, column=1)

#Define hour refine window
class HourWindow(ttk.Frame):
    """Allows users to filter which hours the restaurant should be open"""
    def __init__(self, parent):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        #Initialize the slider variables
        self.startVar = tk.IntVar()
        self.endVar = tk.IntVar()
        #Create and add hour sliders
        self.startScale = tk.Scale(self, variable = self.startVar, from_=1, to =24, orient="horizontal", label="Open From:") 
        self.endScale = tk.Scale(self, variable = self.endVar, from_=1, to =24, orient="horizontal", label="Open To:") 
        self.startScale.grid(row=0, column=0)
        self.endScale.grid(row=0, column=1)
        
#Define category refine window
class CategoryWindow(ttk.Frame):
    '''Allows users to further refine filter based on the restaurant categories.'''
    def __init__(self, parent):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        #Create check buttons variable
        catCheckVar = tk.StringVar() #used to get the on/off value of the checkbutton
        #Initialize the instance variables for the data
        self.categories = ["cat1", "cat2", "cat3", "cat4", "cat5", "cat6", "cat7", "cat8", "cat9"]
        ##Create and add category label
        self.categoryLabel = ttk.Label(self, text="Categories:")
        self.categoryLabel.grid(row=0, column=0)
        #Method to create and add category refinement
        def addCategory(self):
            row = 0
            column = 1
            for category in self.categories:
                tk.Checkbutton(self, text=category, onvalue=category, variable=catCheckVar).grid(row=row, column=column, sticky="W")
                if column == 1:
                    column = 2
                else:
                    row += 1
                    column = 1

        addCategory(self)

#Define neighborhood refine window
class NeighborhoodWindow(ttk.Frame):
    '''Allows users to further refine filter based on neighborhood.'''
    def __init__(self, parent):
        """Sets up window, widgets, and data."""
        super().__init__(parent)
        #Create check buttons variable
        hoodCheckVar = tk.StringVar() #used to get the on/off value of the checkbutton
        #Initialize the instance variables for the data
        self.hoods = ["hood1", "hood2", "hood3", "hood4", "hood5", "hood6", "hood7", "hood8", "hood9"]
        ##Create and add category label
        self.hoodLabel = ttk.Label(self, text="Neighborhoods:")
        self.hoodLabel.grid(row=0, column=0)
        #Method to create and add category refinement
        def addHoods(self):
            row = 0
            column = 1
            for hood in self.hoods:
                tk.Checkbutton(self, text=hood, onvalue=hood, variable=hoodCheckVar).grid(row=row, column=column, sticky="W")
                if column == 1:
                    column = 2
                else:
                    row += 1
                    column = 1

        addHoods(self)

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
        self.refineWindow = RefineWindow(self)
        self.hourWindow = HourWindow(self)
        self.categoryWindow = CategoryWindow(self)
        self.neighborhoodWindow = NeighborhoodWindow(self)
        #Add widgets
        self.searchWindow.pack()
        self.filterWindow.pack()
        self.refineWindow.pack()
        self.hourWindow.pack()
        self.categoryWindow.pack()
        self.neighborhoodWindow.pack()
        #Run the program
        self.mainloop()

#Automatically run program
if __name__ == "__main__":
    Main()
