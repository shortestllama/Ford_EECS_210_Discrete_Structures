'''
EECS 210 Assignment 5
Checks to see if a given relation is a function
and if so, what type of function and if able,
returns an inverse function
Inputs: none
Outputs: the sets, function, whether or not it
is a function, what type of function, and the
inverse function
Jack Ford
10/27/2022
'''
'''
function that returns whether or not a given
function is a function
'''
def is_function(s1, s2, f): #initializes the is_function function
    check = [] #initializes a list to check against

    for i in f: #loops through all the values in the function
        check.append(i[0]) #adds all the first values of the function to the check list

    for i in s1: #loops through all the values in the first set
        if check.count(i) != 1: #checks to see if the values in the check list are not equal to 1
            return False #returns false

    return True #returns true
'''
function that returns whether or not a given
function is injective
'''
def is_injective(s1, s2, f): #initializes the is_injective function
    for i in f: #loops through all the values in the function
        for j in f: #loops through all the values in the function
            if i[1] == j[1]: #checks to see if the second value in both function calls are the same
                if i[0] != j[0]: #checks to see if the first value in both function calls are not the same
                    return False #returns false

    return True #returns true
'''
function that returns whether or not a given
function is surjective
'''
def is_surjective(s1, s2, f): #initializes the is_surjective function
    check = [] #initializes a list to check against

    for i in f: #loops through all the values in the function
        check.append(i[1]) #adds all the second values of the function to the check list

    for i in s2: #loops through all the values in the second set
        if i not in check: #checks to see if the values in the second set are not in the check list
            return False #returns false

    return True #returns true
'''
function that returns whether or not a given
function is bijective
'''
def is_bijective(s1, s2, f): #initializes the is_bijective function
    if is_injective(s1, s2, f) and is_surjective(s1, s2, f): #checks to see if the function is injective and surjective
        return True #returns true

    return False #returns false
'''
function that returns the inverse of a given
function
'''
def inverse_function(s1, s2, f): #initializes the inverse_function function
    ans = {(0, 0)} #initializes an answer set with a tuple
    ans.remove((0, 0)) #removes the initial tuple in the answer set

    for i in f: #loops through all the values in the function
        ans.add((i[1], i[0])) #adds the inverse of the tuple in the given function to the answer set

    return ans #returns the answer
'''
function that prints the desired output on
the given input examples
'''
def ans(a, b, f): #initializes the ans function
    print('A = ', a) #prints the first set
    print('B = ', b) #prints the second set
    print('f = ', f) #prints the function

    if is_function(a, b, f): #checks to see if the given function is a function
        print('The relation is a function') #prints that the given function is a function

        if is_bijective(a, b, f): #checks to see if the given function is bijective
            print('The relation is bijective') #prints that the given function is bijective
            print('f-1 = ', inverse_function(a, b, f)) #prints the inverse function of the given function

        elif is_injective(a, b, f): #checks to see if the given function is injective
            print('The relation is injective') #prints that the given function is injective

        elif is_surjective(a, b, f): #checks to see if the given function is surjective
            print('The relation is surjective') #prints that the given function is surjective

    else:
        print('The relation is not a function') #prints that the given relation is not a function
'''
main function that defines all the given
input examples and calls the ans function
on each of them
'''
def main():
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    v = 'v'
    w = 'w'
    x = 'x'
    y = 'y'
    z = 'z'
    a1 = {a, b, c, d}
    a2= a1
    a3 = a1
    a4 = a1
    a5= {a, b, c}
    a6 = a1
    a7 = a1
    a8 = a1
    a9 = a5
    b1 = {v, w, x, y, z}
    b2 = {x, y, z}
    b3 = {w, x, y, z}
    b4 = {1, 2, 3, 4, 5}
    b5 = {1, 2, 3, 4}
    b6 = {1, 2, 3}
    b7 = b5
    b8 = b5
    b9 = b5
    f1= {(a, z), (b, y), (c, x), (d, w)}
    f2 = {(a, z), (b, y), (c, x), (d, z)}
    f3 = f1
    f4 = {(a, 4), (b, 5), (c, 1), (d, 3)}
    f5 = {(a, 3), (b, 4), (c, 1)}
    f6 = {(a, 2), (b, 1), (c, 3), (d, 2)}
    f7 = {(a, 4), (b, 1), (c, 3), (d, 2)}
    f8 = {(a, 2), (b, 1), (c, 2), (d, 3)}
    f9 = {(a, 2), (b, 1), (a, 4), (c, 3)}

    a_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
    b_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    f_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9]

    for i in range(9):
        ans(a_list[i], b_list[i], f_list[i])
if __name__ == '__main__':
    main()