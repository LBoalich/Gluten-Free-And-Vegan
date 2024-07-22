#Imports
from restaurant import Restaurant

#Create Restaurants class
class Restaurants():
    """Represents all of the restaurants."""
    def __init__(self, restaurantList):
        """Constructor creates a list of restaurant objects, a list of categories, a list of neighborhoods, and tracks the minimum and maximum entree prices."""
        self.restaurants = []
        self.categories = []
        self.neighborhoods = []
        self.minPrice = 2000
        self.maxPrice = 0
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
    #Define filter modules
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
            if min >= priceRange[0] and max <= priceRange[1]:
                restaurantList.append(restaurant)
        return restaurantList
    def hasSpecials(self):
        """Returns the restaurants that have specials."""
        restaurantList = []
        for restaurant in self.restaurants:
            if restaurant.getSpecials() != None:
                restaurantList.append(restaurant)
        return restaurantList

#Instantiate list that holds restaurants
restaurantList = [{"name": "Sanctuary Bistro", "website": "www.sanctuarybistro.com","address": "6414 Rea Road C2 \nCharlotte, NC 28277", "phone": "(980)335-0908", "hours": {"Wednesday": [[1130, 1500], [1730, 2100]], "Thursday": [[1130, 1500], [1730, 2100]], "Friday": [[1130, 1500], [1730, 2100]], "Saturday": [[1000, 1500], [1730, 2100]]}, "category": "Vegan", "neighborhood": "Piper Glen", "price": [13, 22], "specials": None}, {"name": "Oh My Soul", "website": "https://ohmysoulusa.com","address": "3046 N Davidson St.\nCharlotte, NC 28205", "phone": "(704)891-4664", "hours": {"Tuesday": [[1200, 1600], [1700, 2100]], "Wednesday": [[1200, 1600], [1700, 2100]], "Thursday": [[1200, 1600], [1700, 2100]], "Friday": [[1200, 1600], [1700, 2200]], "Saturday": [[1000, 2200]], "Sunday": [[1000, 1630]]}, "category": "Vegan", "neighborhood": "Noda", "price": [15, 25], "specials": None}]

#Define function that creates restaurants object for testing purposes.  Will be deleted.
def main():
    """Create restaurants object from a list of restaurant dictionaries."""
    restaurants = Restaurants(restaurantList)
    print(restaurants.getCategories())
    print(restaurants.getNeighborhoods())
    print(restaurants.getMinPrice())
    print(restaurants.getMaxPrice())
    print(restaurants.categoryMatch("Vegan"))
    print(restaurants.hasSpecials())
    print(restaurants.neighborhoodMatch("Noda"))
    print(restaurants.priceRangeMatch(15, 24))


#Runs program automatically when file is opened. For testing purposes, will be deleted.
if __name__ == "__main__":
    main()
