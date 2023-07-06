from fonctions import *
import math
def test_multiplication():
    # Test avec des nombres positifs
    input_num1 = 2
    input_num2 = 3
    expected_output = 6
    
    assert multiplication(input_num1,input_num2) == expected_output
      
        
        # Test avec des nombres null
    input_num1 = 2
    input_num2 = 0
    expected_output = 0
    
    assert multiplication(input_num1,input_num2) == expected_output
    
        
        # Test avec des nombres negatif
    input_num1 = 2
    input_num2 = -3
    expected_output = -6
   
    assert multiplication(input_num1,input_num2) == expected_output
        
   
        
def test_division():
            
         # Test avec 1
    input_num1 = 10
    input_num2 = 1
    expected_output = 10
    
    assert division(input_num1,input_num2) == expected_output
        
        
        
         # Test avec des nombres positifs
    input_num1 = 18
    input_num2 = 2
    expected_output = 9
    
    assert division(input_num1,input_num2) == expected_output
        

        
         # Test avec des nombres positifs
    input_num1 = 6
    input_num2 = -3
    expected_output = -2
    
    assert division(input_num1,input_num2) == expected_output
       
        
         # Test avec le nombre null 
    input_num1 = 15
    input_num2 = 0
    expected_output = "Erreur : Division par zéro"
    try:
        division(input_num1,input_num2)
    except TypeError:
        print('Test case 3 passed.')
    else:
        print('Test case 3 failed.')
        
def test_addition():
            
         # Test avec 1
    input_num1 = 10
    input_num2 = 1
    expected_output = 11
    
    assert addition(input_num1,input_num2) == expected_output
        
        
        
         # Test avec des nombres positifs
    input_num1 = 18
    input_num2 = 2
    expected_output = 20
    
    assert addition(input_num1,input_num2) == expected_output
    
    
        
         # Test avec le nombre nul 
    input_num1 = 15
    input_num2 = 0
    expected_output = 0
    
    assert addition(input_num1,input_num2) == expected_output
       
 

def test_soustraction():
            
         # Test avec 1
    input_num1 = 10
    input_num2 = 1
    expected_output = 9
    
    assert soustraction(input_num1,input_num2) == expected_output
       
        
        
         # Test avec des nombres positifs
    input_num1 = 18
    input_num2 = 2
    expected_output = 16
    
    assert soustraction(input_num1,input_num2) == expected_output
        
        
         # Test avec le nombre nul 
    input_num1 = 15
    input_num2 = 0
    expected_output = 15
    
    assert soustraction(input_num1,input_num2) == expected_output
        
       