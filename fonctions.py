def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b
    
# Fonction de multiplication 
def multiplication(a, b):
    return a * b

# Fonction de division
def division(a, b):
    if b != 0:
        return a / b
    else:
        raise  TypeError('"Erreur : division par zéro"')

def puissance(a,n):
    try:
        return a**n
    except TypeError:
        return "Les entree doivent etre des nombres"