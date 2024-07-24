import tkinter as tk
from tkinter import ttk

#Define filter results window class
class ResultsWindow(ttk.Frame):
    """Allows user to see results from filter and choose a restaurant to get more information"""
    def __init__(self, parent,controller):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        #Initializes the results data
        self.resultsList = ["name1", "name2", "name3", "name4", "name5"]
        #Create and add the label widget
        self.resultsLabel = ttk.Label(self, text="Results")
        self.resultsLabel.grid(row=0, column=0, columnspan=2)
        #Create method to create and add the results
        def addResults(self):
            self.resultVar = tk.StringVar()
            self.resultVar.set(self.resultsList[0])
            row = 1
            column = 0
            for result in self.resultsList:
                tk.Radiobutton(self, text=result, variable=self.resultVar, value=result).grid(row=row, column=column)
                if column == 0:
                    column += 1
                else:
                    row += 1
                    column = 0  
            return row     
        self.lastRow = addResults(self)
        #Create and add see more info button
        self.infoButton = ttk.Button(self, text="See More Info", command=lambda :infoCommand(self))
        self.infoButton.grid(row=(self.lastRow + 1), column=0, columnspan=2)
        #Create command method for info button
        def infoCommand(self):
            return
