#Imports
from restaurant import Restaurant

#Create Restaurants class
class Restaurants():
    """Represents all of the restaurants."""
    def __init__(self, restaurantList):
        """Constructor creates a list of restaurant objects, a list of categories, a list of neighborhoods, and tracks the minimum and maximum entree prices."""
        self.restaurants = []
        self.names = []
        self.categories = []
        self.neighborhoods = []
        self.minPrice = 2000 #Initialze to value extremely large to not auto filter out matches
        self.maxPrice = 0 #Initialize to free to not auto filter out matches
        for restaurant in restaurantList:
            name = restaurant["name"]
            website = restaurant["website"]
            address = restaurant["address"]
            phone = restaurant["phone"]
            hours = restaurant["hours"]
            category = restaurant["category"]
            neighborhood = restaurant["neighborhood"]
            price = restaurant["price"]
            specials = restaurant["specials"]
            self.restaurants.append(Restaurant(name, website, address, phone, hours, category, neighborhood, price, specials))
            if name not in self.names:
                self.names.append(name)
            if category not in self.categories:
                self.categories.append(category) 
            if neighborhood not in self.neighborhoods:
                self.neighborhoods.append(neighborhood) 
            if price[0] < self.minPrice:
                self.minPrice = price[0]
            if price[1] > self.maxPrice:
                self.maxPrice = price[1]
             
    def __str__(self):
        """Returns the string representation of the restaurants."""
        restaurantsString = "RESTAURANTS:\n\n"
        for restaurant in self.restaurants:
            restaurantsString += str(restaurant) + "\n\n"
        restaurantsString += "CATEGORIES:\n\n"
        for category in self.categories:
            restaurantsString += category + "\n"
        restaurantsString += "\nNEIGHBORHOODS:\n\n"
        for neighborhood in self.neighborhoods:
            restaurantsString += neighborhood + "\n"
        restaurantsString += "\nLOWEST ENTREE PRICE: $" + str(self.minPrice) + "\nHIGHEST ENTREE PRICE: $" + str(self.maxPrice)
        return restaurantsString
    #Define the getters:
    def getNames(self):
        """Returns the restaurant name list."""
        return self.names
    def getCategories(self):
        """Returns the restaurant category list."""
        return self.categories   
    def getNeighborhoods(self):
        """"Returns the neighborhoods list."""
        return self.neighborhoods
    def getMinPrice(self):
        """Returns the lowest entree price."""
        return self.minPrice
    def getMaxPrice(self):
        """Returns the highest entree price."""
        return self.maxPrice
    def getRestuarants(self):
        """Returns the restuaruant list."""
        return self.restaurants
    #Define filter modules
    def nameMatch(self, name):
        """Returns the restaurant object whose name matches the given name."""
        for restaurant in self.restaurants:
            if restaurant.getName() == name:
                return restaurant
    def categoryMatch(self, filterCategories):
        """Returns the restaurant objects that match the filter categories picked by the user."""
        restaurantList = []
        for restaurant in self.restaurants:
            if restaurant.getCategory() in filterCategories:
                restaurantList.append(restaurant)
        return restaurantList
    def neighborhoodMatch(self, filterNeighborhoods):
        """Returns the restaurant objects that match the filter neighborhoods picked by the user."""
        restaurantList = []
        for restaurant in self.restaurants:
            if restaurant.getNeighborhood() in filterNeighborhoods:
                restaurantList.append(restaurant)
        return restaurantList
    def priceRangeMatch(self, min, max):
        """Returns a list of restaurants that fall into the given minimum and maximum prices."""
        restaurantList = []
        for restaurant in self.restaurants:
            priceRange = restaurant.getPrice()
            if min <= priceRange[0] and max >= priceRange[1]:
                restaurantList.append(restaurant)
        return restaurantList
    def hasSpecials(self):
        """Returns the restaurants that have specials."""
        restaurantList = []
        for restaurant in self.restaurants:
            if restaurant.getSpecials() != None:
                restaurantList.append(restaurant)
        return restaurantList
    def hoursMatch(self, minHour, maxHour):
        """Return the restaurants that are open during the given time frame."""
        restaurantList = []
        for restaurant in self.restaurants:
            hours = restaurant.getHours()
            for value in hours.values():
                for hourList in value:
                    if hourList != "Closed":
                        if restaurant not in restaurantList and hourList[0] <= minHour and hourList[1] >= maxHour:
                            restaurantList.append(restaurant)
        return restaurantList
'''
#Define function that creates restaurants object for testing purposes.  Will be deleted.
def main():
    """Create restaurants object from a list of restaurant dictionaries."""
    restaurants = Restaurants(restaurantList)
    hourMatch = restaurants.hoursMatch(1130, 1500)
    for restaurant in hourMatch:
        print(restaurant)



#Runs program automatically when file is opened. For testing purposes, will be deleted.
if __name__ == "__main__":
    main()
'''