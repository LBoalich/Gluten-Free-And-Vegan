from restaurants import Restaurants
from home import HomePage
from refine import RefineWindow
from results import ResultsWindow

#Create controlller class
class Controller():
    """Controlls interactions between the GUI and Restaurants class."""
    def __init__(self, root, restaurantList):
        """Sets up the root, model, and windows."""
        self.root = root
        self.model = Restaurants(restaurantList)
        self.windows = {}
        self.home = self.windows["HopePage"]
        self.refine = self.windows["Refine"]
        self.results = self.windows["Results"]
        #Fill the window dictionary
        for window in (HomePage, RefineWindow, ResultsWindow):
            windowName = window.__name__
            frame = window(self.root, controller=self)
            self.windows[windowName] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #Set the home page as the current window
        self.setWindow("HomePage")
    #Define module to set the current window shown
    def setWindow(self, window):
        currentWindow = self.windows[window]
        currentWindow.tkraise()
