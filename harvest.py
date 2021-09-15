############
# Part 1   #
###########

class MelonType(object):
    """A species of melon at a melon farm."""

    known_melons = set()
    # make a list of tuple at the class level
    #when call method add pairing

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.know_this_melon()
        # make a list of tuple to iterate with entered info

        self.pairings = []

        # Fill in the rest
    def know_this_melon(self):
        self.known_melons.add(self.name)



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend([pairing])
        #add the name and pairing as a tuple to list of pairing at class level

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        return self.code
        



musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
crenshaw1 = MelonType("cren", 1996, "green", False, False, "Crenshaw")
watermelon = MelonType("water", 1996, "green", False, False, "Watermelon")
cantelope = MelonType("cant", 1811, "orange", "False", 'True', "cantelope")

# musk.add_pairing("cheese")
# print(musk.pairings)
# print(MelonType.known_melons)


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = list(MelonType.known_melons)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    print() #how to call method from melontype?
    #use tuple 

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {MelonType.name: MelonType.code} #key melon name, value melon code
    for melon in melon_types:
        if melon == melon.keys():
            return melon.value()

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



