'''
EECS 210 Assignment 3
Performs the required operations on given relations
Inputs: none
Outputs: the result or truth of the required operations on
the given relations
Jack Ford
09/29/2022
'''
'''
function that returns the composition of two given
relations
'''
def composition(r1, r2): #initialize the composition method
    ans = {(0, 0)} #initializes the return variable as a set
    ans.remove((0, 0)) #removes the initial value used to initialize the type of the variable

    for set in r2: #loops through the second relation
        for s in r1: #loops through the first relation
            if set[1] == s[0]: #checks to see if the second value of the second relation equals the first value of the first relation
                ans.add((set[0], s[1])) #adds the firt value of the first relation and the second value of the second relation to the solution variable

    return ans #return the solution variable

'''
function that returns if a relation is reflexive
'''
def is_reflexive(r): #initialize the is_reflexive method
    for i in r: #loops through the relation
        if i[0] != i[1]: #checks to see if the first value of the relation is not equal to the second value of the relation
            return False #returns false

    return True #returns true

'''
function that returns if a function is symmetric
'''
def is_symmetric(r): #initialize the is_symmetric method
    for i in r: #loops through the relation
        for j in r: #loops through the relation
            if i != (j[1], j[0]): #checks to see if a value in the relation is not equal to any other value in the relation with it's values flipped
                return False #returns false

    return True #returns true

'''
function that returns if a function is antisymmetric
'''
def is_antisymmetric(r): #initialize the is_antrisymmetric method
    for i in r: #loops through the relation
        for j in r: #loops through the relation
            if i == (j[1], j[0]): #checks to see if a value in the relation is equal to any other value in the relation with it's values flipped
                return False #returns false

    return True #returns true

'''
function that returns if a function is transitive
'''
def is_transitive(r): #initialize the is_transitive method
    for i in r: #loops through the relation
        for j in r: #loops through the relation
            if i[1] == j[0]: #checks to see if the second value of one value in the relation is equal to the first value of any other value in the relation
                for k in r: #loops through the relation
                    if k != (i[0], j[1]): #checks to see if a third value in the relation is not equal to the first value of the one value in the relation and the second value of any other value in the relation
                        return False #returns false

    return True #returns true

'''
main function that initializes all the relations
and prints the return values of all the required
operations
'''
def main(): #initialize the main method
    r1 = {(1, 1), (2, 2), (3, 3)} #initializes the first relation
    r2 = {(1, 1), (1, 2), (1, 3), (1, 4)} #initializes the second relation
    print('1a. Union of R1 and R2') #prints a description
    print(r1.union(r2)) #prints the union of the two relations
    print('1b. Intersection of R1 and R2') #prints a description
    print(r1.intersection(r2)) #prints the intersection of the two relations
    print('1c. Difference of R1 and R2') #prints a description
    print(r1 - r2) #prints the difference of the first and second relations
    print('1d. Difference of R2 and R1') #prints a description
    print(r2 - r1) #prints the difference of the second and first relations
    r = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)} #initializes the first relation
    s = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)} #initializes the second relation
    print('2. Composition of S and R') #prints a description
    print(composition(s, r)) #prints the composition of the second and first relations
    print('3. Composition of R and R') #prints a description
    print(composition(r, r)) #prints the composition of the first and second relations
    domain = {-10} #initializes the domain with the first value
    
    for i in range(-9, 11): #loops through all the values that are meant to be in the domain
        domain.add(i) #adds the intended values to the domain

    rel = {(0, 0)} #initializes the relation

    for i in domain: #loops through the domain
        for j in domain: #loops through the domain
            if i + j == 0: #checks to see if the one value in the domain plus any other value is equal to 0
                rel.add((i, j)) #adds the values to the relation

    print('4a. Ordered pair of R') #prints a description
    print(rel) #prints the relation
    print('4b. Reflexivity of R') #prints a description
    print(is_reflexive(rel)) #prints if the relation is reflexive
    print('4c. Symmetry of R') #prints a description
    print(is_symmetric(rel)) #prints if the relation is symmetric
    print('4d. Antisymmetry of R') #prints a description
    print(is_antisymmetric(rel)) #prints if the relation is antisymmetric
    print('4e. Transitivity of R') #prints a description
    print(is_transitive(rel)) #prints if the relation is transitive

if __name__ == '__main__': #checks to see if the file contains a main function
    main() #calls the main function