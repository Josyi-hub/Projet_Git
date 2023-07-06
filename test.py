from fonctions import *
import math
def test_multiplication():
    # Test avec des nombres positifs
    input_num1 = 2
    input_num2 = 3
    expected_output = 6
    try:
        assert multiplication(input_num1,input_num2) == expected_output
        print("Test case 1 passed.")
    except AssertionError:
        print("Test case 1 failed.")
        
        
        # Test avec des nombres null
    input_num1 = 2
    input_num2 = 0
    expected_output = 0
    try:
        assert multiplication(input_num1,input_num2) == expected_output
        print("Test case 2 passed.")
    except AssertionError:
        print("Test case 2 failed.")
        
        # Test avec des nombres negatif
    input_num1 = 2
    input_num2 = -3
    expected_output = -6
    try:
        assert multiplication(input_num1,input_num2) == expected_output
        print("Test case 3 passed.")
    except AssertionError:
        print("Test case 3 failed.")
        
def test_division():
            
         # Test avec 1
    input_num1 = 10
    input_num2 = 1
    expected_output = 10
    try:
        assert division(input_num1,input_num2) == expected_output
        print("Test case 1 passed.")
    except AssertionError:
        print("Test case 1 failed.")
        
        
         # Test avec des nombres positifs
    input_num1 = 18
    input_num2 = 2
    expected_output = 9
    try:
        assert division(input_num1,input_num2) == expected_output
        print("Test case 2 passed.")
    except AssertionError:
        print("Test case 2 failed.")
        
         # Test avec des nombres positifs
    input_num1 = 6
    input_num2 = -3
    expected_output = -2
    try:
        assert division(input_num1,input_num2) == expected_output
        print("Test case 3 passed.")
    except AssertionError:
        print("Test case 3 failed.")
        
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
    try:
        assert addition(input_num1,input_num2) == expected_output
        print("Test case 1 passed.")
    except AssertionError:
        print("Test case 1 failed.")
        
        
         # Test avec des nombres positifs
    input_num1 = 18
    input_num2 = 2
    expected_output = 20
    try:
        assert addition(input_num1,input_num2) == expected_output
        print("Test case 2 passed.")
    except AssertionError:
        print("Test case 2 failed.")
        
         # Test avec le nombre nul 
    input_num1 = 15
    input_num2 = 0
    expected_output = 15
    try:
        assert addition(input_num1,input_num2) == expected_output
        print("Test case 3 passed.")  
    except AssertionError:
        print("Test case 3 failed.")

def test_soustraction():
            
         # Test avec 1
    input_num1 = 10
    input_num2 = 1
    expected_output = 9
    try:
        assert soustraction(input_num1,input_num2) == expected_output
        print("Test case 1 passed.")
    except AssertionError:
        print("Test case 1 failed.")
        
        
         # Test avec des nombres positifs
    input_num1 = 18
    input_num2 = 2
    expected_output = 16
    try:
        assert soustraction(input_num1,input_num2) == expected_output
        print("Test case 2 passed.")
    except AssertionError:
        print("Test case 2 failed.")
        
         # Test avec le nombre nul 
    input_num1 = 15
    input_num2 = 0
    expected_output = 15
    try:
        assert soustraction(input_num1,input_num2) == expected_output
        print("Test case 3 passed.") 
    except AssertionError:
        print("Test case 3 failed.")     
       
       # Appel des fonctions de test
print("Test Multiplication")
test_multiplication()
print("Test Division")
test_division() 
print("Test Addition")
test_addition() 
print("Test Soustraction")
test_soustraction() 
        
    