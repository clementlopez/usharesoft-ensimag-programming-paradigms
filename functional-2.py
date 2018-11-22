#!/usr/bin/env python3 

# higher order functions: functions that take a function as parameter, or functions that return other functions. Funception.

import json

def beer_sort(beers, beerCompare):
    if len(beers) <= 1:
        return beers
    else:
        return beer_sort([lt for lt in beers[1:] if beerCompare(lt, beers[0]) < 0], beerCompare) + \
            beers[0:1] + \
            beer_sort([gt for gt in beers[1:] if beerCompare(gt, beers[0]) >= 0], beerCompare)

def beer_comparator(key):
    return lambda b1, b2: 0 if b1[key] == b2[key] else -1 if b1[key] < b2[key] else 1

def print_json(data):
    print(json.dumps(data))

with open("beer_list.json") as f:
    beers = json.load(f)

beers_with_alcool = list(filter(lambda b: b['Tx_Alcool'] is not None, beers))

print_json(beer_sort(beers_with_alcool, beer_comparator('Tx_Alcool')))
