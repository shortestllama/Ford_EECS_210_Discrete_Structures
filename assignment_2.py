'''
EECS 210 Assignment 2
Python code for the proofs of 10 propositions
Inputs: none
Outputs: proofs of 10 propositions
Jack Ford
09/15/2022
'''
'''
method that checks to see if at least one
of the numbers in the domain is true for
the given statement
'''
def one_a(domain): #initializes the method for 1a
    for i in domain: #loops through all the numbers in the domain
        if i < 2: #checks to see if the condition for 1a is true for some of the numbers in the domain
            print(i) #prints the value that proves the condition
            return True #return True

    return False #return False

'''
method that checks to see if at least one
of the numbers in the domain is false for
the given statement
'''
def one_b(domain): #initializes the method for 1b
    for i in domain: #loops through all the numbers in the domain
        if i >= 2: #checks to see if the condition is false for any of the numbers in the domain
            print(i) #prints the value that proves the condition
            return False #return False

    return True #return True

'''
method that checks to see if at least one
of the numbers in the domain is true for
the given statement
'''
def one_c(domain): #initializes the method for 1c
    for i in domain: #loops through all the numbers in the domain
        if i < 2 or i > 7: #checks to see if the condition for 1c is true for some of the numbers in the domain
            print(i) #prints the value that proves the condition
            return True #return True

    return False #return False

'''
method that checks to see if at least one
of the numbers in the domain is false for
the given statement
'''
def one_d(domain): #initializes the method for 1d
    for i in domain: #loops through all the numbers in the domain
        if i >= 2 and i <= 7: #checks to see if the condition is false for any of the numbers in the domain
            print(i) #prints the value that proves the condition
            return False #return False

    return True #return True

'''
method that checks to see if at least one
of the numbers in the domain is false for
the given statement
'''
def one_e(domain): #initializes the method for 1e
    for i in domain: #loops through all the numbers in the domain
        if i < 5: #checks to see if the condition for 1e is true for some of the numbers in the domain
            print(i) #prints the value that proves the condition
            return False #return False

    return True #return True

'''
method that checks to see if at least one
of the numbers in the domain is true for
the given statement
'''
def one_f(domain): #initializes the method for 1f
    for i in domain: #loops through all the numbers in the domain
        if i >= 5: #checks to see if the condition is false for any of the numbers in the domain
            print(i) #prints the value that proves the condition
            return True #return True

    return False #return False

'''
method that checks to see if at least one
of the numbers in both domains are false for
the given statement
'''
def two_a(domain): #initializes the method for 2a
    for i in domain: #loops through all the numbers in the domain
        for j in domain: #loops through all the numbers in the domain
            if i * j != 0: #checks to see if the condition is false for any of the numbers in the domain
                print(i, j) #prints the values that prove the condition
                return False #return False

    return True #return True

'''
method that checks to see if at least one
of the numbers in the first domain is
false for the given statement
'''
def two_b(domain): #initializes the method for 2b
    for i in domain: #loops through all the numbers in the domain
        if i * domain[0] != 0: #checks to see if the condition is false for any of the numbers in the domain for the first number in the domain
            print(i, domain[0]) #prints the values that prove the condition
            return False #return False

    print(i, domain[0]) #prints the values that prove the condition
    return True #return True

'''
method that checks to see if at least one
of the numbers in the second domain is
false for the given statement
'''
def two_c(domain): #initializes the method for 2c
    for i in domain: #loops through all the numbers in the domain
        if domain[0] * i != 0: #checks to see if the condition is false for the first number in the domain for any of the numbers in the domain
            print(domain[0], i) #prints the values that prove the condition
            return False #return False

    print(domain[0], i) #prints the values that prove the condition
    return True #return True

'''
method that checks to see if at least one
of the numbers in both domains are true for
the given statement
'''
def two_d(domain): #initializes the method for 2d
    for i in domain: #loops through all the numbers in the domain
        for j in domain: #loops through all the numbers in the domain
            if i * j == 0: #checks to see if the condition for 2d is true for some of the numbers in the domain
                print(i, j) #prints the values that prove the condition
                return True #return True

    return False #return False

'''
main method that initializes the domain,
prints all the statements,
and calls all the functions'''
def main(): #initializes the main method
    domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #initializes the domain with all the numbers in the domain

    print('1a') #prints the number for the next problem
    print(one_a(domain)) #prints the return statement after calling the next function and passing in the domain
    print('1b') #prints the number for the next problem
    print(one_b(domain)) #prints the return statement after calling the next function and passing in the domain
    print('1c') #prints the number for the next problem
    print(one_c(domain)) #prints the return statement after calling the next function and passing in the domain
    print('1d') #prints the number for the next problem
    print(one_d(domain)) #prints the return statement after calling the next function and passing in the domain
    print('1e') #prints the number for the next problem
    print(one_e(domain)) #prints the return statement after calling the next function and passing in the domain
    print('1f') #prints the number for the next problem
    print(one_f(domain)) #prints the return statement after calling the next function and passing in the domain
    print('2a') #prints the number for the next problem
    print(two_a(domain)) #prints the return statement after calling the next function and passing in the domain
    print('2b') #prints the number for the next problem
    print(two_b(domain)) #prints the return statement after calling the next function and passing in the domain
    print('2c') #prints the number for the next problem
    print(two_c(domain)) #prints the return statement after calling the next function and passing in the domain
    print('2d') #prints the number for the next problem
    print(two_d(domain)) #prints the return statement after calling the next function and passing in the domain
    
if __name__ == '__main__': #checks to see if the file can be run
    main() #runs the main function