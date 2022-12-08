# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
import gilded_rose_refact as gr

class GildedRoseTest(unittest.TestCase):

    def test_class(self):
        items = [gr.NormalItem("foo", 0, 0),gr.Queso("Aged Brie",0,0),gr.Sulfuras("Sulfuras, Hand of Ragnaros",0,0),gr.EntradaAlBackstage("Backstage passes to a TAFKAL80ETC concert",0,0),gr.Conjured("Conjured Mana Cake",0,0)]
        gilded_rose = gr.GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)
        self.assertEquals("Aged Brie", items[1].name)
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[2].name)
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[3].name)
        self.assertEquals("Conjured Mana Cake", items[4].name)

    def test_conjured(self):
        items = [gr.Conjured("Conjured", -2, 10),gr.Conjured("Conjured", 1, 10),gr.Conjured("Conjured", 1, 0)]
        gilded_rose = gr.GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].quality)
        self.assertEquals(8, items[1].quality)
        self.assertEquals(0, items[2].quality)
    
    

        
if __name__ == '__main__':
    unittest.main()