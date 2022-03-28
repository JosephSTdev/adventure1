class Inventory:
    def __init__(self, gold=0):
        self.storage = {}
        self.gold = gold
    def clear(self):
        self.storage.clear()
    def withdraw(self,item):
        if item in self.storage:
            quantity, itemClass = self.storage[item]
            if (quantity-1 == 0):
                del self.storage[item]
            else:
                self.storage[item] = (quantity-1,itemClass)
            return True
        return False
    def insert(self, itemClass):
        self.storage[itemClass.getItemName()] = (1,itemClass)
