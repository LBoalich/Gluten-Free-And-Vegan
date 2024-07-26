import tkinter as tk
from tkinter import ttk

#Define results checkbuttons window class
class ResultsCheckbuttonsWindow(ttk.Frame):
    """Allows user to see results from filter."""
    def __init__(self, parent, controller):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller
        #Set up the grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        #Initializes the results data
        self.resultsList = self.controller.getFinalResults()
    #Create method to create and add the results
    def addResults(self):
        self.resultsList = self.controller.getFinalResults()
        if len(self.resultsList) > 0:
            self.resultVar = tk.StringVar()
            self.resultVar.set(self.resultsList[0])
            row = 0
            column = 0
            for result in self.resultsList:
                tk.Radiobutton(self, text=result, variable=self.resultVar, value=result).grid(row=row, column=column)
                if column == 0:
                    column += 1
                else:
                    row += 1
                    column = 0 
        else:
            self.noResultsLabel = ttk.Label(text="No Results").pack()
