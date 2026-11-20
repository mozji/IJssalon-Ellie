def presenteer (dictionary, totaal) : 
    for naam, bedrag in dictionary.items() :
        print (f"{naam.capitalize()} : {bedrag} euro")

    print (f"\nTotaal: {totaal} euro")