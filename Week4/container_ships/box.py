class Box:
    """ Initializate classs Box """
    def __init__(self,items):
        self.items = items
        
    def describe(self):
        return f" item: {self.items}, "
        