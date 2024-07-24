from restaurants import Restaurants
from home import HomePage
from refine import RefineWindow
from results import ResultsWindow
from search import SearchWindow
from filter import FilterWindow
from hour import HourWindow
from category import CategoryWindow
from neighborhood import NeighborhoodWindow
from price import PriceWindow
from specials import SpecialsWindow

#Create controlller class
class Controller():
    """Controlls interactions between the GUI and Restaurants class."""
    def __init__(self, root, restaurantList):
        """Sets up the root, model, and windows."""
        self.root = root
        self.restaurants = Restaurants(restaurantList)
        self.windows = {}
        #Fill the window dictionary
        for window in (HomePage, RefineWindow, ResultsWindow):
            windowName = window.__name__
            frame = window(self.root, controller=self)
            self.windows[windowName] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #Create all of the windows
        self.home = self.windows["HomePage"]
        self.refine = self.windows["RefineWindow"]
        self.results = self.windows["ResultsWindow"]
        self.search = SearchWindow(self.home, self)
        self.filter = FilterWindow(self.home, self)
        self.hour = HourWindow(self.refine, self)
        self.category = CategoryWindow(self.refine, self)
        self.neighborhood = NeighborhoodWindow(self.refine, self)
        self.price = PriceWindow(self.refine, self)
        self.specials = SpecialsWindow(self.refine, self)
        #Set the home page as the current window
        self.setWindow("HomePage")
    #Define module to set the current window shown
    def setWindow(self, window):
        currentWindow = self.windows[window]
        currentWindow.tkraise()
    #Define module to get list of categories
    def getCategoryList(self):
        categories = self.restaurants.getCategories()
        return categories
    #Define module to get list of neighborhoods
    def getNeighborhoodList(self):
        neighborhoods = self.restaurants.getNeighborhoods()
        return neighborhoods
