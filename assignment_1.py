'''
EECS 210 Assignment 1
Python code for the truth tables of 6 separate propositions
Inputs: none
Outputs: truth tables for all 6 propositions
Jack Ford
08/30/2022
'''
'''
method that loops through 8 times to create 8
separate strings that get printed as the truth
table for demorgans first law
'''
def DM_first_law(): #initializes the method to print demorgans first law
    p = True #initializes p as True
    q = True #initializes q as True
    r = True #initializes r as True
    solution = ['!p\t!q\tp*q\t!(p*q)\t!p+!q'] #initializes the solution list with the first line that defines each function
    print("r\tp\tq\t" + solution[0]) #prints the top line of the table which defines each column

    for i in range(8): #loops 8 times
        solution.append(str(not p) + '\t' + str(not q) + '\t' + str(p and q) + '\t' + str(not (p and q)) + '\t' + str((not p) or (not q))) #adds a line to the list with the values of the function in each column
        print(str(r) + '\t' + str(p) + '\t' + str(q) + '\t' + solution[i + 1]) #prints each row's values
        
        q = not q #changes q each iteration so that it covers all combinations of r, p, and q

        if i % 2 != 0: #checks if i is odd
            p = not p #changes p every other iteration so that it covers all combinations of r, p, and q

        if i == 3: #checks if i is 3
            r = not r #changes r after the fourth iteration so that it covers all combinations of r, p, and q
'''
method that loops through 8 times to create 8
separate strings that get printed as the truth
table for demorgans second law
'''
def DM_second_law(): #initializes the method to print demorgans second law
    p = True #initializes p as True
    q = True #initializes q as True
    r = True #initializes r as True
    solution = ['!p\t!q\tp+q\t!(p+q)\t!p*!q'] #initializes the solution list with the first line that defines each function
    print("r\tp\tq\t" + solution[0]) #prints the top line of the table which defines each column

    for i in range(8): #loops 8 times
        solution.append(str(not p) + '\t' + str(not q) + '\t' + str(p or q) + '\t' + str(not (p or q)) + '\t' + str((not p) and (not q))) #adds a line to the list with the values of the function in each column
        print(str(r) + '\t' + str(p) + '\t' + str(q) + '\t' + solution[i + 1]) #prints each row's values
        
        q = not q #changes q each iteration so that it covers all combinations of r, p, and q

        if i % 2 != 0: #checks if i is odd
            p = not p #changes p every other iteration so that it covers all combinations of r, p, and q

        if i == 3: #checks if i is 3
            r = not r #changes r after the fourth iteration so that it covers all combinations of r, p, and q
'''
method that loops through 8 times to create 8
separate strings that get printed as the truth
table for the first associative law
'''
def first_associative(): #initializes the method to print the first associative law
    p = True #initializes p as True
    q = True #initializes q as True
    r = True #initializes r as True
    solution = ['p*q\tq*r\t(p*q)*r\tp*(q*r)'] #initializes the solution list with the first line that defines each function
    print("r\tp\tq\t" + solution[0]) #prints the top line of the table which defines each column

    for i in range(8): #loops 8 times
        solution.append(str(p and q) + '\t' + str(p and r) + '\t' + str((p and q) and r) + '\t' + str(p and (q and r))) #adds a line to the list with the values of the function in each column
        print(str(r) + '\t' + str(p) + '\t' + str(q) + '\t' + solution[i + 1]) #prints each row's values
        
        q = not q #changes q each iteration so that it covers all combinations of r, p, and q

        if i % 2 != 0: #checks if i is odd
            p = not p #changes p every other iteration so that it covers all combinations of r, p, and q

        if i == 3: #checks if i is 3
            r = not r #changes r after the fourth iteration so that it covers all combinations of r, p, and q
'''
method that loops through 8 times to create 8
separate strings that get printed as the truth
table for the second associative law
'''
def second_associative(): #initializes the method to print the second associative law
    p = True #initializes p as True
    q = True #initializes q as True
    r = True #initializes r as True
    solution = ['p+q\tq+r\t(p+q)+r\tp+(q+r)'] #initializes the solution list with the first line that defines each function
    print("r\tp\tq\t" + solution[0]) #prints the top line of the table which defines each column

    for i in range(8): #loops 8 times
        solution.append(str(p or q) + '\t' + str(p or r) + '\t' + str((p or q) or r) + '\t' + str(p or (q or r))) #adds a line to the list with the values of the function in each column
        print(str(r) + '\t' + str(p) + '\t' + str(q) + '\t' + solution[i + 1]) #prints each row's values
        
        q = not q #changes q each iteration so that it covers all combinations of r, p, and q

        if i % 2 != 0: #checks if i is odd
            p = not p #changes p every other iteration so that it covers all combinations of r, p, and q

        if i == 3: #checks if i is 3
            r = not r #changes r after the fourth iteration so that it covers all combinations of r, p, and q
'''
method that loops through 8 times to create 8
separate strings that get printed as the truth
table for the fifth proposition
'''
def number_five(): #initializes the method to print the fifth proposition
    p = True #initializes p as True
    q = True #initializes q as True
    r = True #initializes r as True
    solution = ['p+q\tp->q\tq->r\t((p+q)*(p->r)*(q->r))->r'] #initializes the solution list with the first line that defines each function
    print("r\tp\tq\t" + solution[0]) #prints the top line of the table which defines each column

    for i in range(8): #loops 8 times
        solution.append(str(p or q) + '\t' + str(q or not p) + '\t' + str(r or not q) + '\t' + str(r or not((p or q) and (r or not p) and (r or not q)))) #adds a line to the list with the values of the function in each column
        print(str(r) + '\t' + str(p) + '\t' + str(q) + '\t' + solution[i + 1]) #prints each row's values
        
        q = not q #changes q each iteration so that it covers all combinations of r, p, and q

        if i % 2 != 0: #checks if i is odd
            p = not p #changes p every other iteration so that it covers all combinations of r, p, and q

        if i == 3: #checks if i is 3
            r = not r #changes r after the fourth iteration so that it covers all combinations of r, p, and q
'''
method that loops through 8 times to create 8
separate strings that get printed as the truth
table for the sixth proposition
'''
def con_prop(): #initializes the method to print the sixth proposition
    p = True #initializes p as True
    q = True #initializes q as True
    r = True #initializes r as True
    solution = ['p->q\tq->p\tp<->q\t(p->q)*(q->p)'] #initializes the solution list with the first line that defines each function
    print("r\tp\tq\t" + solution[0]) #prints the top line of the table which defines each column

    for i in range(8): #loops 8 times
        solution.append(str(q or not p) + '\t' + str(p or not q) + '\t' + str((q and p) or (not q and not p)) + '\t' + str((q or not p) and (p or not q))) #adds a line to the list with the values of the function in each column
        print(str(r) + '\t' + str(p) + '\t' + str(q) + '\t' + solution[i + 1]) #prints each row's values
        
        q = not q #changes q each iteration so that it covers all combinations of r, p, and q

        if i % 2 != 0: #checks if i is odd
            p = not p #changes p every other iteration so that it covers all combinations of r, p, and q

        if i == 3: #checks if i is 3
            r = not r #changes r after the fourth iteration so that it covers all combinations of r, p, and q
'''
main function that calls each truth table function,
separated by a line declaring what each truth table
represents
'''
def main(): #initializes the main function
    print("De Morgan's First Law") #prints the title for the first proposition
    DM_first_law() #calls the function for the first proposition
    print("De Morgan's Second Law") #prints the title for the second proposition
    DM_second_law() #calls the function for the first proposition
    print("First Associative Law") #prints the title for the third proposition
    first_associative() #calls the function for the first proposition
    print("Second Associative Law") #prints the title for the fourth proposition
    second_associative() #calls the function for the first proposition
    print("True Proposition") #prints the title for the fifth proposition
    number_five() #calls the function for the first proposition
    print("Congruent Proposition") #prints the title for the sixth proposition
    con_prop() #calls the function for the first proposition

if __name__ == "__main__": #check to see if this is a runnable program
    main() #call the main function