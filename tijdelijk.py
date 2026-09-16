from helper import decoreer

def print_aanbieding ():
    Prijzen = {
        "aardbei":3,
        "vanille":4,
        "chocolade":5
    }

    aanbieding = Prijzen ["aardbei"] * 0.8

    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter-slechts € {aanbieding}"

    reclame_tekst2 = reclame_tekst [:61]
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split()
    for el in reclame_tekst4:
        if len(el)>=5:
            print (el.upper())
        else:
            print (el.lower())
    print (reclame_tekst2)
    print (reclame_tekst3)
    print (reclame_tekst4)

decoreer ("aanbieding")
print_aanbieding ()
