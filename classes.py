class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display two pieces of information"""
        print(f"The name of a restaurant is {self.restaurant_name}")
        print(f"It serves {self.cuisine_type.title()} cuisine")

    def open_restaurant(self):
        """Display information about a restaurant"""
        print(f"{self.restaurant_name.title()} is open serving {self.cuisine_type.title()} food.")


restaurant1 = Restaurant('Bella Napoli', 'italian')
restaurant2 = Restaurant('Uncle Julio', 'mexican')
restaurant3 = Restaurant('Avocado Queen', 'european')
restaurant4 = Restaurant('Egg Harbor', 'American')

restaurant1.open_restaurant()
restaurant1.describe_restaurant()
print(restaurant1.cuisine_type.title())


class School:
    """Initializing a simple attempt to describe school"""

    def __init__(self, name, year, type):
        self.name = name
        self.year = year
        self.type = type

    def year_founded(self):
        print(f'{self.name} was founded in {self.year}. It is a {self.type} school.')
        print(f'{self.name} is the best school out there.')

school1 = School('MDIST', 2008, 'university')
school2 = School("Wales", 1876, 'primary')

school1.year_founded()
school2.year_founded()

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Describe the user"""
        print(f"User's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        """Display a personalized greeting to the user"""
        print(f"Hello, {self.first_name}, we are so happy to see you here!")

user1 = User('Ahmet', 'Guclu')
user2 = User('Nigora', 'Rustamova')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()









