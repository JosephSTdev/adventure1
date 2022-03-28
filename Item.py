from email.errors import NoBoundaryInMultipartDefect
from mimetypes import init


class Item:
    def __init__(self,name):
        self.itemName = name
    def getItemName(self):
        return self.itemName