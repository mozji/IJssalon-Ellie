import csv


from helper import decoreer, onderstreep, som
from presentatie import presenteer 

mijn_dict= {"Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750}

totaal = 5250

presenteer (mijn_dict, totaal)

voorraad = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
    }

print (voorraad)

totaal_inkomsten = som (voorraad)

print (f"Totaal inkomen: {totaal_inkomsten}")

with open ("boekhouding.csv", "w", newline="") as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([key, value])
