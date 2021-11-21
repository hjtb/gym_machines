class Bird(object):
    """
    Bird superclass
    """
    def __init__(self, kind, call):
        # instance attributes
        self.kind = kind
        self.call = call

    def description(self):
        """
        Returns description string including instance attributes
        """
        return f'A {self.kind} goes {self.call}'


class Fowl(Bird):
    """
    Subclass of the superclass Bird
    """
    def __init__(self, kind, call, type):
        self.fowl_types = {'landfowl': 'Landfowl is an order of heavy-bodied ground-feeding birds that includes\n'
                                       'turkey, grouse, chicken, New World quail and Old World quail,\n'
                                       'ptarmigan, partridge, pheasant, junglefowl and the Cracidae\n',
                           'waterfowl': 'Waterfowl is an order of birds that comprises about 180 living species\n'
                                        'in three families: Anhimidae (the screamers), Anseranatidae\n'
                                        '(the magpie goose), and Anatidae,the largest family, which\n'
                                        'includes over 170 species of waterfowl,\n'
                                        'among them the ducks, geese, and swans.\n'}
        self.type = type
        # Uses super() function to state kind, call from superclass Bird
        super().__init__(kind, call)


    def description(self):
        """
        Returns string from superclass description method and
        appends a string to include additional information
        """
        return f'{super().description()} \nSome interesting facts about the {self.kind} : A {self.kind} is of type {self.type}. {self.fowl_types[self.type.lower()]}'

class Seabird(Bird):
    """
    Subclass of Bird superclass for sea birds
    """
    def __init__(self, kind, call, diving_depth):
        # super() is used to denote what is inherited from Bird
        super().__init__(kind, call)
        self.diving_depth = diving_depth

    def get_description(self):
        """
        Returns description from superclass using super() function
        Appends additional information as a string
        """
        return f'{super().description()} and also, a {self.kind} dives to a depth of {self.diving_depth} metres.'


gannet = Seabird('Gannet', 'Squawk', 3)
print(gannet.get_description())

duck = Fowl('Mallard', 'Quack!', 'Waterfowl')
print(duck.description())