class Box:
    """ Initializate classs Box """
    def __init__(self,item_name, item_id, item_description, items_per_box):
        self.item_name = item_name
        self.item_id = item_id
        self.item_description = item_description
        self.items_per_box = items_per_box
        
        
    def describe(self):
        return f"item name: {self.item_name}, item id: {self.item_id}, item description: {self.item_description}, items per box: {self.items_per_box}; "
        