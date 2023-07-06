def addition(a,b):
    if type(a)!=float | type(b)!=float:
        raise TypeError("Veuillez entrez des nombres")
    return a+b

def division(a,b):
    if b==0:
        raise TypeError("On ne divise pas par zero")
    return a/b
    
