#Create restaurant class
class Restaurant():
    """Represents a restaurant."""
    def __init__(self, name, website, address, phone, hours, category, neighborhood, price, specials = None):
        """Constructor creates a restaurant with the given name, website, address, phone number, hours, category, neighborhood, entree price range, and specials which is instantiated to None if omitted."""
        self.name = name
        self.website = website
        self.address = address
        self.phone = phone
        self.hours = hours
        self.category = category
        self.neighborhood = neighborhood
        self.price = price
        self.specials = specials
    def __str__(self):
        """Returns the string representation of the restaurant."""
        return "Name: " + self.name + \
               "\nWebsite: " + self.website + \
               "\nAddress: " + self.address + \
               "\nPhone Number: " + self.phone + \
               "\nHours:" + self.stringHours() + \
               "\nCategory: " + self.category + \
               "\nNeighborhood: " + self.neighborhood + \
               "\nEntree Price Range: " + self.stringPrice() + \
               "\nSpecials: " + self.stringSpecials()
    #Define the getters:
    def getName(self):
        """Returns the restaurant's name."""
        return self.name
    def getWebsite(self):
        """"Returns the restaurant's website."""
        return self.website
    def getAddress(self):
        """"Returns the restaurant's address."""
        return self.address
    def getPhone(self):
        """"Returns the restaurant's phone number."""
        return self.phone
    def getHours(self):
        """"Returns the restaurant's hours."""
        return self.hours
    def getCategory(self):
        """"Returns the restaurant's category."""
        return self.category
    def getNeighborhood(self):
        """"Returns the restaurant's neighborhood."""
        return self.neighborhood
    def getPrice(self):
        """"Returns the restaurant's entree price range."""
        return self.price
    def getSpecials(self):
        """"Returns the restaurant's specials or None if they do not offer specials."""
        return self.specials
    #Define modules that returns string representations
    def stringHours(self):
        """Returns the string representation of hours."""
        stringHours = ""
        for (key, value) in self.hours.items():
            stringHours += ("\n" + key + ":") 
            for openClose in value:
                open = self.militaryToStandard(openClose[0])
                close = self.militaryToStandard(openClose[1])
                stringHours += ("\n" + open + " to " + close)
        return stringHours
    def stringPrice(self):
        return ("$" + str(self.price[0]) + " to $" + str(self.price[1]))
    def stringSpecials(self):
        if self.specials == None:
            return "None"
        else:
            return "Fix this later."
    #Define module to turn military time to standard time
    def militaryToStandard(self, time):
        """Converts military time to standard time in string format."""
        if time < 1300: #Represents am time
            stringTime = str(time)
            standardTime = stringTime[0:2] + ":" + stringTime[2:] + "am"
        else: 
            time -= 1200 #Represents pm time
            stringTime = str(time)
            if time < 1000:
                standardTime = stringTime[0] + ":" + stringTime[1:] + "pm"
            else:
                standardTime = stringTime[0:2] + ":" + stringTime[2:] + "pm"
        return standardTime

#Instantiate list that holds restaurants
restaurantList = [{"name": "Sanctuary Bistro", "website": "www.sanctuarybistro.com","address": "6414 Rea Road C2 \nCharlotte, NC 28277", "phone": "(980)335-0908", "hours": {"Wednesday": [[1130, 1500], [1730, 2100]], "Thursday": [[1130, 1500], [1730, 2100]], "Friday": [[1130, 1500], [1730, 2100]], "Saturday": [[1000, 1500], [1730, 2100]]}, "category": "Vegan", "neighborhood": "Piper Glen", "price": [13, 22]}]

#Define function that creates a list of restaurant objects
def main():
    """Creates a list of restaurant objects from a list of restaurant dictionaries."""
    restaurantObjects = []
    for restaurant in restaurantList:
        name = restaurant["name"]
        website = restaurant["website"]
        address = restaurant["address"]
        phone = restaurant["phone"]
        hours = restaurant["hours"]
        category = restaurant["category"]
        neighborhood = restaurant["neighborhood"]
        price = restaurant["price"]
        restaurantObjects.append(Restaurant(name, website, address, phone, hours, category, neighborhood, price))
    for restaurant in restaurantObjects:
        print(restaurant)

#Runs program automatically when file is opened. For testing purposes.
if __name__ == "__main__":
    main()
