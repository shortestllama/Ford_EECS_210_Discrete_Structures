'''
EECS 210 Assignment 8
Outputs a few graph algorithms and the game
of nim
Inputs: none
Outputs: the results of the graph algorithms
and the results of the game of nim
Jack Ford
12/8/2022
'''
def is_empty(l):
    if len(l) == 0: #checks to see if the length is 0
        return True

    return False
    
def get_degrees(graph):
    degrees = {}

    for i in graph: #loops through all the values in the graph
        degrees[i[0]] = 0 #sets the dictionary value at the 0th i value to 0
        degrees[i[1]] = 0 #sets the dictionary value at the 1st i value to 0

    for i in graph: #loops through all the values in the graph
        degrees[i[0]] += 1 #adds one to the dictionary value at the 0th i value
        degrees[i[1]] += 1 #adds one to the dictionary value at the 1st i value

    return degrees

def has_euler_circuit(graph):
    degrees = get_degrees(graph) #get the degree values for each vertex of the graph

    for i in degrees.values(): #loops through all the degree values of the graph
        if i % 2 != 0: #checks to see if the degree value is odd
            return False

    return True

def get_odd_degrees(graph):
    ans = []
    degrees = get_degrees(graph) #gets the degree values for each vertex of the graph

    for i in degrees.values(): #loops through all the degree values of the graph
        if i % 2 != 0: #checks to see if the degree value is odd
            ans.append(i) #adds the degree value to the list

    for i in ans: #loops through all the values of the list
        print(list(degrees.keys())[list(degrees.values()).index(i)]) #prints the key at the given value
        degrees.pop(list(degrees.keys())[list(degrees.values()).index(i)]) #removes the item at the given key at the given value

def print_euler_circuit(graph):
    ans = ''
    graph = list(graph)
    circuit = [graph[0]]

    while circuit[0][0] != circuit[len(circuit) - 1][1]: #continues until the circuit is complete
        for i in graph: #loops through all the values in the graph
            if circuit[len(circuit) - 1][1] == i[0]: #checks to see if the last value in the circuit is equal to the next one in the graph
                circuit.append(i) #adds the next value in the graph to the circuit

    H = set(graph).difference(set(circuit)) #creates a new graph of the difference of the old one and the circuit
    H = list(H)

    while not is_empty(H): #checks to see if the new graph is empty
        subcircuit = [H[0]]

        for i in H: #loops through all the values in the new circuit
            while subcircuit[len(subcircuit) - 1][1] != subcircuit[0][0]: #loops until the circuit is complete
                if subcircuit[len(subcircuit) - 1][1] == i[0]: #checks to see if the next value in the graph comes after the last value in the circuit
                    subcircuit.append(i) #adds the value to the circuit

        H = set(H).difference(set(subcircuit)) #creates a new graph of the difference of the old one and the circuit
        H = list(H)

        for i in circuit: #loops through all the values in the circuit
            if i[1] == H[0][0]: #checks to see if the subcircuit precedes the given value
                ind = circuit.index(i) #sets the index to the given value the subcircuit precedes

        for i in subcircuit: #loops through all the values in the subcircuit
            circuit.insert(ind, i) #inserts the subcircuit where it belongs in the circuit
            ind += 1 #increments the index for the next value of the subcircuit

    for i in circuit: #loops through all the values of the circuit
        ans = ans + i[0] + '-' #formats the answer

    ans += circuit[0][0] #formats the end of the answer

    print(ans) #prints the answer

def has_hamilton_circuit(graph):
    degrees = get_degrees(graph) #gets the degree values for each vertex of the graph
    
    if len(degrees.keys()) >= 3: #checks to see if the graph has at least three vertices
        n = len(degrees.keys()) #sets the number of vertices equal to n

        for i in degrees.values(): #loops through all the values of the degrees
            if i < (n / 2): #checks to see if the value of the degree is less than half the number of vertices
                return False

        return True

    return False

def has_hamilton_circuit_ore(graph):
    degrees = get_degrees(graph) #gets the degree values for each vertex of the graph

    if len(degrees.keys()) >= 3: #checks to see if the graph has at least three vertices
        n = len(degrees.keys()) #sets the number of vertices equal to n
        checks = []

        for i, k in enumerate(degrees.keys()): #loops through all the values of the vertices
            for j in list(degrees.keys())[i + 1::]: #loops through all the values of the vertices
                checks.append((k, j)) #adds all the combinations of vertices to the check variable

        for i in checks: #loops through all the combinations of vertices
            if i not in graph and (i[1], i[0]) not in graph: #checks to see if the two vertices are adjacent
                if degrees[i[0]] + degrees[i[1]] < n: #checks to see if the sum of the two degrees of the vertices is less than the total number of vertices
                    return False

        return True

    return False

def check_graph(graph):
    if has_euler_circuit(graph):
        print_euler_circuit(graph)

    else:
        get_odd_degrees(graph)

    print('\n')

def next(player):
    if player == 1: #checks to see if the current player is player 1
        return 2

    return 1

def move(state, pile, n):
    temp = []

    for i in state: #loops through all the values in the current game state
        temp.append(i) #adds the values to the temp variable

    for i in range(1, len(state) + 1): #loops through all the possible pile values
        if i == pile: #checks to see if the given value matches the pile
            if n <= state[i - 1]: #checks to see if the value to change by is less than or equal to the value in the pile
                temp[i - 1] = temp[i - 1] - n #updates the temp game state by the number to change the pile by

    return temp

def is_legal_move(state, pile, num):
    for i in range(1, len(state) + 1): #loops through all the possible pile values
        if i == pile: #checks to see if the given value matches the pile
            if state[i - 1] >= num: #checks to see if the value to change by is less than or equal to the value in the pile
                if move(state, pile, num) != [0, 0, 0]: #checks to see if the move would create an invalid game state
                    return True

    return False

#pile, move
def legal_moves(state):
    temp = []

    for i in state: #loops through all the values in each pile
        temp.append(i) #adds each pile value to the temp variable

    ans = []

    for i in range(1, len(state) + 1): #loops through all the possible pile values
        for j in range(1, state[i - 1] + 1): #loops through all the possible move values
            if is_legal_move(state, i, j): #checks to see if the move is legal
                ans.append(move(temp, i, j)) #adds the move to the answer

    return ans

def is_finished(state):
    if sum(state) == 1: #checks to see if the game state only has one pile of one
        return True

    return False

def rec_nim(state, player):
    if is_finished(state) and player == 1: #checks to see if the game state is finished and who the current player is
        return -1

    elif is_finished(state) and player == 2: #checks to see if the game state is finished and who the current player is
        return 1

    else:
        temp = []

        for i in legal_moves(state): #loops through all the legal moves
            print(i) #prints the current move
            val = rec_nim(i, next(player)) #recursive call on the current move
            temp.append(val) #adds the returned value to the temp variable

    if player == 1: #checks to see if the current player is player one
        print(max(temp)) #prints the max value of the temp variable
        return max(temp)

    print(min(temp)) #prints the min value of the temp variable
    return min(temp)

def main():
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g = 'g'
    h = 'h'
    i = 'i'
    G1 = [(a,b),(b,e),(e,d),(d,c),(c,e),(e,a)]
    G2 = [(a,b),(b,c),(c,d),(d,a),(a,e),(e,b),(d,e),(e,c)]
    G3 = [(a,b),(b,e),(e,d),(d,c),(c,a),(a,d),(d,b)]
    G4 = [(a,c),(c,d),(d,b),(b,a),(c,a),(a,b),(a,d)]
    check_graph(G1)
    check_graph(G2)
    check_graph(G3)
    check_graph(G4)
    test = [(d,a),(a,b),(b,c),(c,f),(f,i),(i,h),(h,g),(g,d),(d,b),(b,e),(e,f),(f,h),(h,e),(e,d)]
    check_graph(test)
    G5 = [(b,e),(e,c),(c,d),(d,e),(e,a),(a,b),(b,c),(c,a)]
    G6 = [(a,b),(b,c),(c,d),(d,b)]
    G7 = [(a,b),(b,c),(c,d),(b,g),(g,e),(e,c),(e,f)]
    print(has_hamilton_circuit(G5))
    print(has_hamilton_circuit(G6))
    print(has_hamilton_circuit(G7))
    test_2 = [(c,a),(a,b),(b,c),(c,f),(f,e),(e,d),(d,f)]
    print(has_hamilton_circuit(test_2))
    print(has_hamilton_circuit_ore(G5))
    print(has_hamilton_circuit_ore(G6))
    print(has_hamilton_circuit_ore(G7))
    print(has_hamilton_circuit_ore(test_2))
    rec_nim([2, 2, 1], 1)
    print('\n')
    rec_nim([1, 2, 3], 1)
    print('If 1 is the last number, player 1 won. If -1 is the last number, player 2 won')

if __name__ =='__main__':
    main()