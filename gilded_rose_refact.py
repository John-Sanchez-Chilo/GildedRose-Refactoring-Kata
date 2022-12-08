class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def is_expired(self):
        if(self.sell_in <= 0):
            return True
        return False
    
    def set_min_quality(self):
        if(self.quality < 0):
            self.quality = 0

    def set_max_quality(self):
        if(self.quality > 50):
            self.quality = 50
            

    def update_quality(self):
        pass # it will be overriden

class NormalItem(Item):
    def update_quality(self):
        if(self.is_expired()):
            self.quality = self.quality - 2
        else:
            self.quality = self.quality - 1
        self.set_min_quality()
        self.sell_in = self.sell_in - 1

class Queso(Item):
    def update_quality(self):
        if (not self.is_expired()):
            self.quality = self.quality + 1
        else:
            self.quality = self.quality + 2
        self.set_max_quality()
        self.sell_in = self.sell_in - 1

class Sulfuras(Item):
    def update_quality(self):
        pass #it has no change

class EntradaAlBackstage(Item):
    def update_quality(self):
        if(self.is_expired()):
            self.quality = 0
        else:
            self.quality = self.quality + 1
            if(self.sell_in <= 10):
                self.quality = self.quality + 1
            if(self.sell_in <= 5):
                self.quality = self.quality + 1
            self.set_max_quality()
        self.sell_in = self.sell_in - 1

class Conjured(Item):
    def update_quality(self):
        if(self.is_expired()):
            self.quality = self.quality - 4
        else:
            self.quality = self.quality - 2
        self.set_min_quality()
        self.sell_in = self.sell_in - 1

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
