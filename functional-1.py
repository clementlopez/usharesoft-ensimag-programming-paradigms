#!/usr/bin/env python3

# functional programming uses small functions as the primary mean to express your program
# a program is seen as a transformation of data: <data in> --- functions ---> <data out>

# pure functions are highly preferred: functions that always return the same value for the same input

import json

def beer_sort(beers, beerCompare):
    if len(beers) <= 1:
        return beers
    else:
        return beer_sort([lt for lt in beers[1:] if beerCompare(lt, beers[0]) < 0], beerCompare) + \
            beers[0:1] + \
            beer_sort([gt for gt in beers[1:] if beerCompare(gt, beers[0]) >= 0], beerCompare)

with open("beer_list.json") as f:
    beers = json.load(f)

beers_with_alcool = list(filter(lambda b: b['Tx_Alcool'] is not None, beers))

print(json.dumps(beer_sort(beers_with_alcool, lambda b1, b2: b2['Tx_Alcool'] - b1['Tx_Alcool'])))
