#!/usr/bin/python3

import json
from collections import namedtuple
from pprint import pprint

class Biere(object):
    nom = ""
    gout = 0
    amertume = ""
    soif = 0
    tx_alcool = 0
    brasserie = ""
    pays = ""
    fermentation = ""
    remarque = ""

    def __init__(self, nom, gout, amertume, soif, tx_alcool, brasserie, pays, fermentation, remarque):
        self.nom = nom
        self.gout = gout
        self.amertume = amertume
        self.soif = soif
        self.tx_alcool = tx_alcool
        self.brasserie = brasserie
        self.pays = pays
        self.fermentation = fermentation
        self.remarque = remarque

    def __str__(self):
        return ", ".join(("Nom: " + str(self.nom),
                          "Pays: " + str(self.pays),
                          "Brasserie: " + str(self.brasserie),
                          "Tx: " + str(self.tx_alcool),
                          "Gout: " + str(self.gout),
                          "Amertume: " + str(self.amertume),
                          "Soif: " + str(self.soif),
                          "Fermentation: " + str(self.fermentation),
                          "Remarque: " + str(self.remarque)))

    def __repr__(self):
        return self.__str__()


with open('beer_list.json') as f:
    data = json.load(f)

liste_des_bieres = []

for biere in data:
    x = json.loads(json.dumps(biere), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    biere = Biere(x.Nom or "", x.Gout or "", x.Amertume or 0, x.Soif or 0, x.Tx_Alcool or 0, x.Brasserie or "",
                  x.Pays or "", x.Fermentation or "", x.Remarque or "")

    liste_des_bieres.append(biere)

liste_des_bieres.sort(key=lambda biere: (str(biere.pays), float(biere.tx_alcool)))
pprint(liste_des_bieres)
