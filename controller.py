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
        #Create filter category checkbox attributes
        self.hoursVar = 0
        self.categoryVar = 0
        self.neighborhoodVar = 0
        self.priceVar = 0
        self.specialsVar = 0
        #Create filter hour scale variable attributes
        self.minHour = 0
        self.maxHour = 24
        #Create category checkbutton dictionary to hold variable values from refine window
        self.refineCategoryVarDictonary = {}
        #Create filter entree price range scale attributes
        self.minPrice = 5
        self.maxPrice = 200
        #Create results list
        self.finalResults = []
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
    #Define module to get list of categories
    def getCategoryList(self):
        categories = self.restaurants.getCategories()
        return categories
    #Define module to get list of neighborhoods
    def getNeighborhoodList(self):
        neighborhoods = self.restaurants.getNeighborhoods()
        return neighborhoods
    #Define module to get the checked categories in refine window
    def getRefineCategoryChecked(self):
        refineCategoryChecked = []
        for key, value in self.refineCategoryVarDictonary.items():
            if value == 1:
                refineCategoryChecked.append(key)
        return refineCategoryChecked
    #Define module to get the final results
    def getFinalResults(self):
        return self.finalResults
    #Define module to set the current window shown
    def setWindow(self, window):
        currentWindow = self.windows[window]
        currentWindow.tkraise()
    #Define setters for the filter checkbutton variables
    def setHoursVar(self, var):
        self.hoursVar = var
    def setCategoryVar(self, var):
        self.categoryVar = var
    def setNeighborhoodVar(self, var):
        self.neighborhoodVar = var
    def setPriceVar(self, var):
        self.priceVar = var
    def setSpecialsVar(self, var):
        self.specialsVar = var
    #Define setter for the refine category variable dictionary
    def setRefineCategoryVar(self, key, value):
        self.refineCategoryVarDictonary[key] = value
    #Define setter for the final results list
    def setFinalResults(self):
        #Reset final results to empty list
        self.finalResults = []
        #Get the list of restaurants
        restaurantList = self.restaurants.getRestuarants()
        #If hour was selected in filter, set the min and max hour attributes to data selected in refine window and get matches.  Otherwise set hour matches list to all restaurants. 
        if self.hoursVar == 1:
            minScale = self.refine.hourWindow.startScale.get()
            maxScale = self.refine.hourWindow.endScale.get()
            stringMinHour = str(minScale) + "00"
            intMinHour = int(stringMinHour)
            stringMaxHour = str(maxScale) + "00"
            intMaxHour = int(stringMaxHour)
            self.minHour = intMinHour
            self.maxHour = intMaxHour
            hourMatches = self.restaurants.hoursMatch(self.minHour, self.maxHour)
        else: 
            hourMatches = restaurantList
        #If cateogry was selected in filter, get the categories chosen and mathching restaurants.  Otherwise set category matches to all restaurants.
        if self.categoryVar == 1:
            checkedCategories = self.getRefineCategoryChecked()
            categoryMatches = self.restaurants.categoryMatch(checkedCategories)
        else:
            categoryMatches = restaurantList
        #If entree price range selected in filter, get the min and max price and set to the controller attributes, find matches and add to price list.  Otherwise set price matches to all restaurants.
        if self.priceVar == 1:
            self.minPrice = self.refine.priceWindow.lowScale.get()
            self.maxPrice = self.refine.priceWindow.highScale.get()
            priceMatch = self.restaurants.priceRangeMatch(self.minPrice, self.maxPrice)
        else:
            priceMatch = restaurantList
        #Set the final results list based on matches
        for restaurant in restaurantList:
            if (restaurant in hourMatches) and (restaurant in categoryMatches) and (restaurant in priceMatch):
                self.finalResults.append(restaurant)
        #Add the results to the results window
        self.addResultsRadiobuttons()
    #Define module that adds the checked filter categories to the refine window
    def addFilterCategoriesToRefine(self):
        if self.hoursVar == 1:
            self.refine.hourWindow.grid(row=1, column=0)
        if self.categoryVar == 1:
            self.refine.categoryWindow.grid(row=2, column=0)
        if self.neighborhoodVar == 1:
            self.refine.neighborhoodWindow.grid(row=3, column=0)
        if self.priceVar == 1:
            self.refine.priceWindow.grid(row=4, column=0)
        if self.specialsVar == 1:
            self.refine.specialsWindow.grid(row=5, column=0)
    #Define module to add results checkbuttons on refine filter button click
    #Create and add checkbuttons winodw
    def addResultsRadiobuttons(self):
        self.results.resultsRadiobuttons.addResults()
        if len(self.finalResults) > 0:
            self.results.noResultsLabel.destroy()
