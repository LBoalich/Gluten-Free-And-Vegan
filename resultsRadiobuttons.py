import tkinter as tk
from tkinter import ttk, PhotoImage

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
        #Create list to hold the image paths
        self.imageList = []
        #Create list to hold the loaded images
        self.loadImageList = []
        #Set up the grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)   
    #Create method to create and add the result radio buttons
    def addResults(self):
        #Get the results data
        self.resultsList = self.controller.getFinalResults()
        #Populate the image list and loaded image list
        for restuarant in self.resultsList:
            self.image = restuarant.getImage()
            self.imageList.append(self.image)
        for image in self.imageList:
            self.loadImage = tk.PhotoImage(file=image)
            self.loadImageList.append(self.loadImage)
        #If there are restaurants that match the refinement, create and add radiobutton
        if len(self.resultsList) > 0:
            #Variable to track which radiobutton is selected.  First button selected by defualt
            self.resultVar.set(self.resultsList[0]) 
            row = 0 #Sets initial row for first button to be placed
            column = 0 #Sets initial column for first button to be placed
            #Loop through the results, create radiobutton, and add to frame
            for index in range(len(self.resultsList)):
                restaurant = self.resultsList[index]
                #Varaible to get the current restaurant name
                name = restaurant.getName()
                #Create the button
                resultsRadioButton = tk.Radiobutton(self, text=name, variable=self.resultVar, value=name)
                #Add the buttons to the list to prevent garbage collection
                self.resultsRadioButtons.append(resultsRadioButton)
                #Add button to frame
                resultsRadioButton.grid(row=row, column=column)
                #Create label to show image
                self.imageLabel = tk.Label(self, image=self.loadImageList[index])
                #Add the image label to the frame
                self.imageLabel.grid(row=(row+1), column=column)
                #Increments the rows and columns to place the next button
                #label = tk.Label(self, text=image).grid(row=(row+1), column=column)
                if column == 0:
                    column += 1
                else:
                    row += 2
                    column = 0 
    