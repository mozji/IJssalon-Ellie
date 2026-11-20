def decoreer (tekst=""):
    lengte = len (tekst) + 4
    print ()
    print (lengte * "*")
    print (f"* {tekst} *")
    print (lengte * "*")
    print ()

def onderstreep (tekst = ""):
    uit = []
    uit.append (tekst)
    uit.append (len (tekst) * "=")
    return uit

def som (dictionary) :
    totaal = 0

    for waarde in dictionary.values():
        totaal += waarde

    return totaal