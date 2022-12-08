# -*- coding: utf-8 -*-
from __future__ import print_function

import gilded_rose_class as gr

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             gr.NormalItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
             gr.Queso(name="Aged Brie", sell_in=2, quality=0),
             gr.NormalItem(name="Elixir of the Mongoose", sell_in=5, quality=7),
             gr.Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             gr.Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             gr.EntradaAlBackstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             gr.EntradaAlBackstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             gr.EntradaAlBackstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             gr.Conjured(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        gr.GildedRose(items).update_quality()