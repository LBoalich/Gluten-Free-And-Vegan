import tkinter as tk
from tkinter import ttk

#Define results checkbuttons window class
class ResultsRadiobuttonsWindow(ttk.Frame):
    """Allows user to see results from filter."""
    def __init__(self, parent, controller):
        """Sets up the window, widgets, and data."""
        super().__init__(parent)
        self.controller = controller #Create controller
        #Add results list attribute
        self.resultsList = []
        #Add attribute to track results radio button variable
        self.resultVar = tk.StringVar()
        #Add attribute to hold the radio buttons
        self.resultsRadioButtons = []
        #Set up the grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)   
    #Create method to create and add the result radio buttons
    def addResults(self):
        #Get the results data
        self.resultsList = self.controller.getFinalResults()
        #If there are restaurants that match the refinement, create and add radiobutton
        if len(self.resultsList) > 0:
            #Variable to track which radiobutton is selected.  First button selected by defualt
            self.resultVar.set(self.resultsList[0]) 
            row = 0 #Sets initial row for first button to be placed
            column = 0 #Sets initial column for first button to be placed
            #Loop through the results, create radiobutton, and add to frame
            for result in self.resultsList:
                #Varaible to get the current restaurant name
                name = result.getName()
                #Create the button
                resultsRadioButton = tk.Radiobutton(self, text=name, variable=self.resultVar, value=name)
                #Add the buttons to the list to prevent garbage collection
                self.resultsRadioButtons.append(resultsRadioButton)
                #Add button to frame
                resultsRadioButton.grid(row=row, column=column)
                #Increments the rows and columns to place the next button
                if column == 0:
                    column += 1
                else:
                    row += 1
                    column = 0 
    