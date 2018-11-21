import json
from funcy import compose, partial, curry

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

def sort_by_key(key):
    return lambda data: beer_sort(data, beer_comparator(key))

with open("beer_list.json") as f:
    beers = json.load(f)

beers_with_alcool = list(filter(lambda b: b['Tx_Alcool'] is not None, beers))

compose(print_json, curry(sort_by_key)('Tx_Alcool'))(beers_with_alcool)

# function compositions: combining pure functions together to make a sum that's greater than its parts
# function composition can be intimidating, and in the wrong hands can make the code extremely hard to understand. Great power comes great responsibilities.
