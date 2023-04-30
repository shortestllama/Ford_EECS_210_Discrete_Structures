'''
EECS 210 Assignment 6
Recursively solves a given sodoku puzzle
Inputs: any given sodoku puzzle
Outputs: the solution to the given sodoku
puzzle
Jack Ford
11/10/2022
'''
def get_candidates(puzzle, i, j): #get the potential values for the given empty puzzle space
    ans = [1, 2, 3, 4, 5, 6, 7, 8, 9] #initializes a candidate list to all the potential candidate numbers

    for row_val in puzzle[i]: #loops through all the values in the row
        if row_val != '_': #checks to see if the row value is not an empty space
            if int(row_val) in ans: #checks to see if the row value is in the candidate list
                ans.remove(int(row_val)) #removes the row value from the candidate list

    col_vals = [] #initializes an empty column value list

    for k in range(9): #loops through the values 0-8
        col_vals.append(puzzle[k][j]) #adds the given puzzle column value to the column list

    for col_val in col_vals: #loops through all the column values in the column list
        if col_val != '_': #checks to see if the column value is not an empty space
            if int(col_val) in ans: #checks to see if the column value is in the candidate list
                ans.remove(int(col_val)) #removes the column value from the candidate list

    i_range = ((i // 3) + 1) * 3 #initializes the row range to either the first, middle, or last third of the values
    j_range = ((j // 3) + 1) * 3 #initializes the column range to either the first, middle, or last third of the values
    i_ind = i_range - 3 #initializes the starting row value to 3 less than the row range
    j_ind = j_range - 3 #initializes the starting column value to 3 less than the column range

    while i_ind < i_range: #loops through all three values in the given row range
        while j_ind < j_range: #loops through all three values in the given column range
            if puzzle[i_ind][j_ind] != '_': #checks to see if the puzzle value is not empty
                if int(puzzle[i_ind][j_ind]) in ans: #checks to see if the puzzle value is in the candidate list
                    ans.remove(int(puzzle[i_ind][j_ind])) #removes the puzzle value from the candidate list

            j_ind += 1 #increments the column index

        i_ind += 1 #increments the row index
        j_ind = j_range - 3 #resets the column index

    return ans #return the answer

def rec_fill_cell(puzzle): #the recursive function to solve the sodoku
    i = 0 #initializes the row value to 0
    j = 0 #initializes the column value to 0

    while i < 9: #checks to see if the row value is less than 9
        while j < 9: #checks to see if the column value is less than 9
            if puzzle[i][j] == '_': #checks to see if the puzzle at the row and column is empty
                candidates = get_candidates(puzzle, i, j) #gets the candidate numbers that could fill the empty spot

                if len(candidates) > 0: #checks to see if there are candidate numbers for the empty spot
                    for val in candidates: #loops through all the candidate numbers
                        puzzle[i][j] = val #sets the empty spot equal to the candidate number

                        if rec_fill_cell(puzzle): #checks to see if the recursive call to fill the sodoku is true
                            return True #returns true

                        else: #otherwise
                            puzzle[i][j] = '_' #makes the spot empty again

                return False #return false

            j += 1 #increment the column value

        i += 1 #increment the row value
        j = 0 #reset the column value

    return True #return true

def convert_to_matrix(file): #converts the input file to a matrix
    puzzle = [] #initializes an empty matrix as the puzzle
    puzzle_file = open(file, 'r') #opens the puzzle file

    for line in puzzle_file: #loops through all the lines of the puzzle file
        line = line.strip(' \n') #removes the end of every line
        temp = line.split(' ') #splits each line into a list
        puzzle.append(temp) #adds each list of the line to the puzzle matrix

    puzzle_file.close() #closes the puzzle file

    return puzzle #returns the puzzle matrix

def main(): #runs all the main functions of the program
    flag = False #set the flag to false

    puzzle1 = convert_to_matrix('puzzle1.txt') #converts the input file to a matrix
    print(f'puzzle 1:\n{puzzle1}') #prints the puzzle matrix
    rec_fill_cell(puzzle1) #calls the recursive function to solve the sodoku

    for i in puzzle1: #loops through the rows in the sodoku
        if '_' in i: #checks to see if the sodoku needs a spot filled
            flag = True #sets the flag to true

        else: #otherwise
            for i in range(9): #loops through the rows of the puzzle
                for j in range(9): #loops through the columns of the puzzle
                    puzzle1[i][j] = int(puzzle1[i][j]) #sets the puzzle value to an integer

    if flag: #checks to see if the flag is true
        print('no solution found') #prints no solution
        flag = False #sets the flag to false

    else: #otherwise
        print(puzzle1) #prints the solved puzzle

    puzzle2 = convert_to_matrix('puzzle2.txt') #converts the input file to a matrix
    print(f'puzzle 2:\n{puzzle2}') #prints the puzzle matrix
    rec_fill_cell(puzzle2) #calls the recursive function to solve the sodoku

    for i in puzzle2: #loops through the rows in the sodoku
        if '_' in i: #checks to see if the sodoku needs a spot filled
            flag = True #sets the flag to true

        else: #otherwise
            for i in range(9): #loops through the rows of the puzzle
                for j in range(9): #loops through the columns of the puzzle
                    puzzle2[i][j] = int(puzzle2[i][j]) #sets the puzzle value to an integer

    if flag: #checks to see if the flag is true
        print('no solution found') #prints no solution
        flag = False #sets the flag to false

    else: #otherwise
        print(puzzle2) #prints the solved puzzle

    puzzle3 = convert_to_matrix('puzzle3.txt') #converts the input file to a matrix
    print(f'puzzle 3:\n{puzzle3}') #prints the puzzle matrix
    rec_fill_cell(puzzle3) #calls the recursive function to solve the sodoku

    for i in puzzle3: #loops through the rows in the sodoku
        if '_' in i: #checks to see if the sodoku needs a spot filled
            flag = True #sets the flag to true

        else: #otherwise
            for i in range(9): #loops through the rows of the puzzle
                for j in range(9): #loops through the columns of the puzzle
                    puzzle3[i][j] = int(puzzle3[i][j]) #sets the puzzle value to an integer

    if flag: #checks to see if the flag is true
        print('no solution found') #prints no solution
        flag = False #sets the flag to false

    else: #otherwise
        print(puzzle3) #prints the solved puzzle

    puzzle4 = convert_to_matrix('puzzle4.txt') #converts the input file to a matrix
    print(f'puzzle 4:\n{puzzle4}') #prints the puzzle matrix
    rec_fill_cell(puzzle4) #calls the recursive function to solve the sodoku

    for i in puzzle4: #loops through the rows in the sodoku
        if '_' in i: #checks to see if the sodoku needs a spot filled
            flag = True #sets the flag to true

        else: #otherwise
            for i in range(9): #loops through the rows of the puzzle
                for j in range(9): #loops through the columns of the puzzle
                    puzzle4[i][j] = int(puzzle4[i][j]) #sets the puzzle value to an integer

    if flag: #checks to see if the flag is true
        print('no solution found') #prints no solution
        flag = False #sets the flag to false

    else: #otherwise
        print(puzzle4) #prints the solved puzzle

    puzzle5 = convert_to_matrix('puzzle5.txt') #converts the input file to a matrix
    print(f'puzzle 5:\n{puzzle5}') #prints the puzzle matrix
    rec_fill_cell(puzzle5) #calls the recursive function to solve the sodoku

    for i in puzzle5: #loops through the rows in the sodoku
        if '_' in i: #checks to see if the sodoku needs a spot filled
            flag = True #sets the flag to true

        else: #otherwise
            for i in range(9): #loops through the rows of the puzzle
                for j in range(9): #loops through the columns of the puzzle
                    puzzle5[i][j] = int(puzzle5[i][j]) #sets the puzzle value to an integer

    if flag: #checks to see if the flag is true
        print('no solution found') #prints no solution
        flag = False #sets the flag to false

    else: #otherwise
        print(puzzle5) #prints the solved puzzle

if __name__ == '__main__':
    main()