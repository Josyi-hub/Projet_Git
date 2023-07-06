from fonctions import *

quitter = 1
while quitter == 1:
    try:
        a = float(input("Entrer le premier nombre :"))
        b = float(input("Entrer le deuxieme nombre :"))
        print('====MENU===')
        print('1. Addition')
        print('2. Soustraction')
        print('3. Multiplication')
        print('4. Division')
        choix = int(input(""))
        while choix not in [1,2,3,4]:
            choix = int(input("Choisissez un element du menu: "))
        if choix == 1 :
            print("result:", addition(a,b))
        elif choix == 2 :
            print("result:", soustraction(a,b))
        elif choix == 3 :
            print("result:", multiplication(a,b))
        elif choix == 4 :
            result =division(a,b)
            print("result:", result)
        quitter = int(input("Saisissez 1 pour continuer et 0 pour quitter :"))
        while quitter not in [1,0]:
            quitter = int(input("Saisissez 1 pour continuer et 0 pour quitter :"))
        
    except:
        if type(a)=='str' or type(b)=='str':
            print("Entrez des nombre")
        elif (b==0):
            print("Division non possible par 0")
        quitter=1