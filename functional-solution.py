import json

def beer_sort(beers, beerCompare):
    if len(beers) <= 1:
        return beers
    else:
        return beer_sort([lt for lt in beers[1:] if beerCompare(lt, beers[0]) < 0], beerCompare) + beers[0:1] + \
            beer_sort([gt for gt in beers[1:] if beerCompare(gt, beers[0]) >= 0], beerCompare)

with open("beer_list.json") as f:
    beers = json.load(f)

beers_with_alcool = list(filter(lambda b: b['Tx_Alcool'] is not None, beers))

print(beer_sort(beers_with_alcool, lambda b1, b2: b2['Tx_Alcool'] - b1['Tx_Alcool']))
