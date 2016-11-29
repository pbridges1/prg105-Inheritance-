# In the first step you will create a parent class. Create a parent class for Office Furniture.
# Set the class variables to be category (desk, chair, filing cabinet would be examples), material, length, width, height, and price.
# Include a method that returns a string about the object.


class OfficeFurniture(object):
    """Will accept category, material, length, width, height, and price"""

    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set__price(self, price):
        self.__price = price

    def set_length(self, length):
        self.__length = length

    def set__width(self, width):
        self.__width = width

    def set__height(self, height):
        self.__height = height

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_price(self):
        return self.__price

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def __str__(self):
        order = ("You ordered a " + self.__category + " made from " + self.__material + " with the measurements of " + str(self.__length) + " inches for length, " + str(self.__width) + " inches for width, and " + str(self.__height) + " inches for height with the price of " + "${:0,.2f}".format(self.__price) + ".")
        return order

# order1 = OfficeFurniture('desk', 'wood', 156, 72, 24, 117.50)
# print order1
#  In the second step create a sub class for Desk include location of drawers (left, right both are options) and number_drawers. Override the parents __str__ method to include drawer location and count.


class Desk(OfficeFurniture):
    """
    tells location of drawers and number of drawers needed.
    """
    def __init__(self, category, material, length, width, height, price, location, number_of_drawers):
        self.__location = location
        self.__number_of_drawers = number_of_drawers
        OfficeFurniture.__init__(self, category, material, length, width, height, price)

    def set_location(self, location):
        self.__location = location

    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def get_number_of_drawers(self):
        return self.__number_of_drawers

    def get_location(self):
        return self.__location

    def __str__(self):
        desk = ("You ordered a " + self.get_category() + " made from " + self.get_material() + " with the measurements of " + str(self.get_length()) + " inches for length, " + str(self.get_width()) + " inches for width, and " + str(self.get_height()) + " inches for height with the price of " + "${:0,.2f}".format(self.get_price()) + ".\n" + "Your drawer location is " + self.__location + " with " + str(self.__number_of_drawers) + " drawers.")
        return desk

# order2 = Desk('desk', 'metal', 42, 26, 30, 279.99, 'left', 3)
# print order2
