def addition(a,b):
    if type(a)!=float | type(b)!=float:
        raise TypeError("Veuillez entrez des nombres")
    return a+b

def soustraction(a,b):
    if type(a)!=float | type(b)!=float:
        raise TypeError("Veuillez entrez des nombres")
    return a-b
    
# Fonction de multiplication 
def multiplication(a, b):
    return a * b

# Fonction de division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : division par zéro"
