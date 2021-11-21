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
    def __init__(self, kind, call, category):
        self._fowl_types = {'landfowl': 'Landfowl is an order of heavy-bodied ground-feeding birds that includes\n'
                                       'turkey, grouse, chicken, New World quail and Old World quail,\n'
                                       'ptarmigan, partridge, pheasant, junglefowl and the Cracidae\n',
                           'waterfowl': 'Waterfowl is an order of birds that comprises about 180 living species\n'
                                        'in three families: Anhimidae (the screamers), Anseranatidae\n'
                                        '(the magpie goose), and Anatidae,the largest family, which\n'
                                        'includes over 170 species of waterfowl,\n'
                                        'among them the ducks, geese, and swans.\n'}
        self.category = category
        # Uses super() function to state kind, call from superclass Bird
        super().__init__(kind, call)

    @property
    def fowl_types(self):
        return self._fowl_types[self.category.lower()]


    def description(self):
        """
        Returns string from superclass description method and
        appends a string to include additional information
        """
        return f'{super().description()} \nSome interesting facts about the {self.kind} : A {self.kind} is of type {self.category}. {self._fowl_types[self.category.lower()]}'


mute = Fowl('Swan', 'honk', 'Waterfowl')
print(mute.description())
print(mute.fowl_types)
