#!/usr/bin/env python3
import json

def swap_index(elt_list, index):
    elt_list[index], elt_list[index + 1] = elt_list[index + 1], elt_list[index]

def bubble_sort(beers, key):
    beers_length = len(beers)
    print(beers_length)
    for i in range(beers_length):
        for j, beer in enumerate(beers[i:]):
            ind = i + j
            if ind + 1 < beers_length and (beer[key] or 0) > (beers[ind + 1][key] or 0):
                swap_index(beers, ind)

with open("beer_list.json") as beers_json:
    beers = json.load(beers_json)
    bubble_sort(beers, "Tx_Alcool")
    print("\n".join([str(x["Tx_Alcool"]) for x in beers]))

