#Imports
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
from result import ResultWindow

#Create controlller class
class Controller():
    """Controlls interactions between the GUI and Restaurants class."""
    def __init__(self, root, restaurantList):
        """Sets up the root, model, and windows."""
        #Create attribute to hold the root
        self.root = root 
        #Create attribute to the list of restaurants
        self.restaurants = Restaurants(restaurantList)
        #Create dictionary to hold the 3 frames (homepage, filter, refine)
        self.windows = {}
        #Create filter category checkbox variable attributes initalized to unchecked
        self.hoursVar = 0
        self.categoryVar = 0
        self.neighborhoodVar = 0
        self.priceVar = 0
        self.specialsVar = 0
        #Create filter hour scale variable attributes
        self.minHour = 0 #Initialized to smalled possible value
        self.maxHour = 24 #Initialized to largest possible value
        #Create category checkbutton dictionary to hold variable values from refine window
        self.refineCategoryVarDictonary = {}
        #Create neighborhood checkbutton dictionary to hold variable values from refine window
        self.neighborhoodsCheckbuttonVariables = {}
        #Create filter entree price range scale variable attributes
        self.minPrice = 5 #Initialized to smalled value
        self.maxPrice = 200 #Initialized to largest value
        #Create attribute for refine specials checkbutton variable initialized to unchecked
        self.refineSpecialsCheckVar = 0
        #Create results list used to hold restaurants that match refinement
        self.finalResults = []
        #Create result radio button variable attribute initialized to empty string
        self.resultRadioVar = ""
        #Fill the window dictionary
        for window in (HomePage, RefineWindow, ResultsWindow):
            #Get the string representation of the name of the window
            windowName = window.__name__
            #Create the window with root as parent and controller set to self
            frame = window(self.root, controller=self)
            #Add frame to the windows dictionary using windowName as key
            self.windows[windowName] = frame
            #Add the frame
            frame.grid(row=0, column=0, sticky="nsew")
        #Create refrence to the windows held in windows dictionary
        self.home = self.windows["HomePage"]
        self.refine = self.windows["RefineWindow"]
        self.results = self.windows["ResultsWindow"]
        #Set the home page as the current window
        self.setWindow("HomePage")
    #Define module to set the current window shown
    def setWindow(self, window):
        #Get the disired window from the windows dictionary
        currentWindow = self.windows[window]
        #Bring the window to the top
        currentWindow.tkraise()
    #Define module to get list of categories
    def getCategoryList(self):
         return self.restaurants.getCategories()
    #Define module to get list of neighborhoods
    def getNeighborhoodList(self):
        return self.restaurants.getNeighborhoods()
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
    #Define setter for the refine neighborhood variable dictionary
    def setRefineNeighborhoodVar(self, key, value):
        self.neighborhoodsCheckbuttonVariables[key] = value.get()
    #Define setter for the refine has specials checkbutton variable
    def setRefineSpecialsCheckbuttonVar(self, var):
        self.refineSpecialsCheckVar = var
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
            #Mutate data so that it matches format "0000" to work in hours match function
            stringMinHour = str(minScale) + "00"
            intMinHour = int(stringMinHour)
            stringMaxHour = str(maxScale) + "00"
            intMaxHour = int(stringMaxHour)
            #Set the controller attributes
            self.minHour = intMinHour
            self.maxHour = intMaxHour
            #Find the restaurants that match
            hourMatches = self.restaurants.hoursMatch(self.minHour, self.maxHour)
        else: 
            hourMatches = restaurantList
        #If cateogry was selected in filter, get the categories chosen and mathching restaurants.  Otherwise set category matches to all restaurants.
        if self.categoryVar == 1:
            checkedCategories = self.getRefineCategoryChecked()
            categoryMatches = self.restaurants.categoryMatch(checkedCategories)
        else:
            categoryMatches = restaurantList
        #If neighborhood was selected in the filter, get the neighborhoods selected and show matching restaurants.  Otherwise set to all restaurants.
        if self.neighborhoodVar == 1:
            onlySelected = []
            for value in self.neighborhoodsCheckbuttonVariables:
                if value != "Off":
                    onlySelected.append(value)
            neighborhoodMatches = self.restaurants.neighborhoodMatch(onlySelected)
        else:
            neighborhoodMatches = restaurantList
        #If entree price range selected in filter, get the min and max price and set to the controller attributes, find matches and add to price list.  Otherwise set price matches to all restaurants.
        if self.priceVar == 1:
            self.minPrice = self.refine.priceWindow.lowScale.get()
            self.maxPrice = self.refine.priceWindow.highScale.get()
            priceMatch = self.restaurants.priceRangeMatch(self.minPrice, self.maxPrice)
        else:
            priceMatch = restaurantList
        #If the filter specials checkbutton was selected and refine has specials checkbutton selected, add matching restaurants to specials list.  Otherwise add all restaurants.
        if self.specialsVar == 1 and self.refineSpecialsCheckVar == 1:
            specialsMatch = self.restaurants.hasSpecials()
        else:
            specialsMatch = restaurantList
        #Set the final results list based on matches
        for restaurant in restaurantList:
            if (restaurant in hourMatches) and (restaurant in categoryMatches) and (restaurant in priceMatch) and (restaurant in specialsMatch) and (restaurant in neighborhoodMatches):
                self.finalResults.append(restaurant)
        #Add the results to the results window
        self.addResultsRadiobuttons()
    #Define setter for the result radio button variable
    def setResultRadioVar(self, var):
        self.resultRadioVar = var
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
    #Define module to add results radiobuttons to results on refine filter button click
    def addResultsRadiobuttons(self):
        self.results.resultsRadiobuttons.addResults()
        #If there are results, remove the no results label
        if len(self.finalResults) > 0:
            self.results.noResultsLabel.destroy()
    #Define module that returns the selected restaurant from results
    def getSelectedRestaurant(self):
        #Loops through all restaurants that matched refine filter
        for result in self.finalResults: 
            #When the restaurant name matches the clicked radio button variable, return the restaurant
            if self.resultRadioVar == result.getName(): 
                return result
    #Define module to open the result window
    def openResultWindow(self):
        ResultWindow(controller=self)
