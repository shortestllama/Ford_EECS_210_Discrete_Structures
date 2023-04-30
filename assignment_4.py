'''
EECS 210 Assignment 4
Checks to see if given relations are reflexive,
symmetric, transitive, equivalently related,
or a poset
Inputs: none
Outputs: whether or not the conditions hold true
for the given relations and the closures on those
relations if not true
Jack Ford
10/13/2022
'''
'''
function that returns if a relation is reflexive on a set
'''
def is_reflexive(r, s): #initializes the method
    for i in s: #loops through all the values in the set
        if (i, i) not in r: #checks to see if the reflexive tuple for the given value in the set is in the relation
            return 'is not reflexive'

    return 'is reflexive'
'''
function that returns the reflexive closure of a relation on a set
'''
def reflexive_closure(r, s): #initializes the method
    check = [] #initializes a list to check which values in the set are not reflexive in the relation
    ans = r #initializes a relation equal to the current relation to be returned as the closure

    for i in s: #loops through all the values in the set
        for j in r: #loops through all the values in the relation
            if i == j[0]: #checks to see if the given value in the set is equal to the first value in the given tuple in the relation
                check.append(i) #adds the given value in the set to the check list

    for i in s: #loops through all the values in the set
        if i not in check: #checks to see if the given value in the set is not already in the relation reflexivly
            ans.add((i, i)) #adds the reflexive tuple for the value in the set not already in the relation

    return ans #returns the closure
'''
function that returns if a relation is symmetric on a set
'''
def is_symmetric(r, s): #initializes the method
    flag = False #initializes a flag to check if a value is in the relation

    for i in r: #loops through all the values in the relation
        for j in r: #loops through all the values in the relation
            if i == (j[1], j[0]): #checks to see if any value in the relation has another value equal to its symmetric value
                flag = True #changes the flag to true

        if not flag: #checks to see if the flag is false
            return 'is not symmetric' #returns is not symmetric

        flag = False #sets the flag to false

    return 'is symmetric' #returns is symmetric
'''
function that returns the symmetric closure of a relation on a set
'''
def symmetric_closure(r, s): #initializes the method
    ans = {(1, 1)} #initializes a variable as a set of tuples
    ans.remove((1, 1)) #removes the first tuple

    for i in r: #loops through all the values in the relation
        ans.add(i) #adds all the values in the relation to the answer

    for i in r: #loops through all the values in the relation
        ans.add((i[1], i[0])) #adds all the values in the relation to the answer in symmetric form

    return ans #returns the answer
'''
function that returns if a relation is antisymmetric on a set
'''
def is_antisymmetric(r, s): #initializes the method
    flag = False #initializes a flag to false

    for i in r: #loops through all the values in the relation
        for j in r: #loops through all the values in the relation
            if i[0] != i[1] and i == (j[1], j[0]): #checks to see if the two values in the tuple are not equal and if the tuple equals another value in the relation that is its symmetric value
                flag = True #sets the flag to true

        if flag: #checks to see if the flag is true
            return 'is not antisymmetric' #returns is not antisymmetric

        flag = False #sets the flag to false

    return 'is antisymmetric' #returns is antisymmetric
'''
function that returns if a relation is transitive on a set
'''
def is_transitive(r, s): #initializes the method
    flag = False #initializes a flag to false

    for i in r: #loops through all the values in the relation
        for j in r: #loops through all the values in the relation
            if i[1] == j[0]: #checks to see if the second value of the first tuple is equal to the first value of the second tuple
                for k in r: #loops through all the values in the relation
                    if k == (i[0], j[1]): #checks to see if the third tuple is equal to the first value of the first tuple and the second value of the second tuple
                        flag = True #sets the flag to true

                if not flag: #checks to see if the flag is false
                    return 'is not transitive' #returns is not transitive

                flag = False #sets the flag to false

    return 'is transitive' #returns is transitive
'''
function that returns the transitive closure of a relation on a set using warshall's algorithm
'''
def transitive_closure(r, s): #initializes the method
    ans = {(0, 0)} #initializes a set of tuples
    ans.remove((0, 0)) #removes the first tuple in the set
    s_check = [] #initializes a list

    for i in s: #loops through all the values in the set
        s_check.append(i) #adds all the values in the set to the list

    s_check.sort() #puts all the values in the list in order
    matrix = [] #initializes a matrix

    for i in range(len(s_check)): #loops through the length of the set
        inside = [] #initializes a list to represent the rows of the matrix

        for j in range(len(s_check)): #loops through the length of the set
            inside.append(False) #sets all the values of the row to false

        matrix.append(inside) #adds the row to the matrix

    for i in r: #loops through all the values in the relation
        for j in range(len(s_check)): #loops through the length of the set
            for k in range(len(s_check)): #loops through the length of the set
                if i[0] == s_check[j]: #checks to see if the first value of the tuple is equal to the given value in the set
                    if i[1] == s_check[k]: #checks to see if the second value of the tuple is equal to the given value in the set
                        matrix[j][k] = True #sets the matrix at the value of the set values checked against to true
                        
    for i in range(len(s_check)): #loops through the length of the set
        for j in range(len(s_check)): #loops through the length of the set
            for k in range(len(s_check)): #loops through the length of the set
                matrix[j][k] = matrix[j][k] or (matrix[j][i] and matrix[i][k]) #warshall's algorithm

    for i in range(len(s_check)): #loops through the length of the set
        for j in range(len(s_check)): #loops through the length of the set
            if matrix[i][j]: #checks to see if the matrix at the given value is true
                ans.add((s_check[i], s_check[j])) #adds a tuple of the set values at the given matrix indeces to the answer

    return ans #returns the answer
'''
function that returns if a relation is an equivalence relation on a set
'''
def is_equivalence_relation(r, s): #initializes the method
    if is_reflexive(r, s) == 'is reflexive' and is_symmetric(r, s) == 'is symmetric' and is_transitive(r, s) == 'is transitive': #checks to see if the relation is reflexive, symmetric, and transitive
        return 'R is an equivalence relation' #returns that the relation is an equivalence relation

    else: #if not all of those
        reason = 'R ' #initializes the reason

        if is_reflexive(r, s) == 'is not reflexive': #checks to see if the relation is not reflexive
            reason += 'is not reflexive' #adds to the reason that the relation is not reflexive
        
        if is_symmetric(r, s) == 'is not symmetric': #checks to see if the relation is not symmetric
            if len(reason) > 2: #checks to see if there is already a reason
                reason += ' and is not symmetric' #adds to the reason that the relation is not symmetric

            else: #if not
                reason += 'is not symmetric' #adds to the reason that the relation is not symmetric
        
        if is_transitive(r, s) == 'is not transitive': #checks to see if the relation is not transitive
            if len(reason) > 2: #checks to see if there is already a reason
                reason += ' and is not transitive' #adds to the reason that the relation is not transitive

            else: #if not
                reason += 'is not transitive' #adds to the reason that the relation is not transitive

        return 'R is not an equivalence relation' + '\n' + reason #returns that the relation is not an equivalence relation and the reason
'''
function that returns if a relation is a poset on a set
'''
def is_poset(r, s): #initializes the method
    if is_reflexive(r, s) == 'is reflexive' and is_antisymmetric(r, s) == 'is antisymmetric' and is_transitive(r, s) == 'is transitive': #checks to see if the relation is reflexive, antisymmetric, and transitive
        return '(S, R) is a poset' #returns that the relation is a poset

    else: #if not all of those
        reason = '(S, R) ' #initializes the reason

        if is_reflexive(r, s) == 'is not reflexive': #checks to see if the relation is not reflexive
            reason += 'is not reflexive' #adds to the reason that the relation is not reflexive
        
        if is_antisymmetric(r, s) == 'is not antisymmetric': #checks to see if the relation is not antisymmetric
            if len(reason) > 7: #checks to see if there is already a reason
                reason += ' and is not antisymmetric' #adds to the reason that the relation is not antisymmetric

            else: #if not
                reason += 'is not antisymmetric' #adds to the reason that the relation is not antisymmetric
        
        if is_transitive(r, s) == 'is not transitive': #checks to see if the relation is not transitive
            if len(reason) > 7: #checks to see if there is already a reason
                reason += ' and is not transitive' #adds to the reason that the relation is not transitive

            else: #if not
                reason += 'is not transitive' #adds to the reason that the relation is not transitive

        return '(S, R) is not a poset' + '\n' + reason #returns that the relation is not a poset and the reason
'''
function that checks all the methods above against certain examples
'''
def main(): #initializes the main method
    s1 = {1, 2, 3, 4} #initializes the first set
    r1 = {(1, 1), (4, 4), (2, 2), (3, 3)} #initializes the first relation
    s2 = {'a', 'b', 'c', 'd'} #initializes the second set
    r2 = {('a', 'a'), ('c', 'c')} #initializes the second relation
    print('R = ', r1) #prints the first relation
    print('R ' + is_reflexive(r1, s1)) #prints if the relation is reflexive
    print('R = ', r2) #prints the second relation
    print('R ' + is_reflexive(r2, s2)) #prints if the relation is reflexive
    print(reflexive_closure(r2, s2)) #prints the reflexive closure of the relation

    r3 = {(1, 2), (4, 4), (2, 1), (3, 3)} #initializes the third relation
    r4 = {(1, 2), (3, 3)} #initializes the fourth relation
    print('R = ', r3) #prints the third relation
    print('R ' + is_symmetric(r3, s1)) #prints if the relation is symmetric
    print('R = ', r4) #prints the fourth relation
    print('R ' + is_symmetric(r4, s1)) #prints if the relation is symmetric
    print(symmetric_closure(r4, s1)) #prints the symmetric closure of the relation

    r5 = {('a', 'b'), ('d', 'd'), ('b', 'c'), ('a', 'c')} #initializes the fifth relation
    s3 = {1, 2, 3} #initializes the third set
    r6 = {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)} #initializes the sixth relation
    print('R = ', r5) #prints the fifth relation
    print('R ' + is_transitive(r5, s2)) #prints if the relation is transitive
    print('R = ', r6) #prints the sixth relation
    print('R ' + is_transitive(r6, s3)) #prints if the relation is transitive
    print(transitive_closure(r6, s3)) #prints the transitive closure of the relation

    r7 = {(1, 1), (2, 2), (2, 3)} #initializes the seventh relation
    s4 = {'a', 'b', 'c'} #initializes the fourth set
    r8 = {('a', 'a'), ('b', 'b'), ('c', 'c'), ('b', 'c'), ('c', 'b')} #initializes the eighth relation
    print('R = ', r7) #prints the seventh relation
    print(is_equivalence_relation(r7, s3)) #prints if the relation is an equivalence relation
    print('R = ', r8) #prints the eighth relation
    print(is_equivalence_relation(r8, s4)) #prints if the relation is an equivalence relation

    r9 = {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)} #initializes the ninth relation
    s5 = {0, 1, 2, 3} #initializes the fifth set
    r10 = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)} #initializes the tenth relation
    print('S = ', s1) #prints the first set
    print('R = ', r9) #prints the ninth relation
    print(is_poset(r9, s1)) #prints if the relation is a poset
    print('S = ', s5) #prints the fifth set
    print('R = ', r10) #prints the tenth relation
    print(is_poset(r10, s5)) #prints if the relation is a poset
'''
starts the program
'''
if __name__ == '__main__': #checks to see if the program has a main function
    main() #runs the main function