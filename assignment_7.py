'''
EECS 210 Assignment 7
Outputs the number of ways a certain type of
objects can fit into another type of boxes
Inputs: none
Outputs: the number of ways to do each output
Jack Ford
11/29/2022
'''
import math
#n = objects, k = boxes

def both_distinguishable(n, k, num_n):
    ans = 0 #initialize the answer

    if n < k: #checks to see if the number of objects is less than the number of boxes
        ans = 1 #reinitializes the answer

        for _ in n: #loops for the amount of times equal to the number of objects
            ans *= k #multiplies the answer by itself and the number of boxes
            k = k - 1 #decrements the number of boxes

    else:
        ans = math.factorial(n) / (((math.factorial(num_n)) ** k) * math.factorial(n - (num_n * k))) #formula to find the number of ways to sort distinguishable objects into distinguishable boxes

    return ans #returns the answer

def boxes_distinguishable(n, k):
    if n < k: #checks to see if the number of objects is less than the number of boxes
        return math.ceil(math.factorial(k) / (math.factorial(k - n) * math.factorial(n))) #formula to find the number of ways to sort indistinguishable objects into distinguishable boxes

    else:
        return math.ceil(math.factorial(k + n - 1) / (math.factorial((k + n - 1) - n) * math.factorial(n))) #formula to find the number of ways to sort indistinguishable objects into distinguishable boxes

def objects_distinguishable(n, k):
    if n < k: #checks to see if the number of objects is less than the number of boxes
        return 1 #returns 1

    else:
        ans = 0 #initialize the answer
        j = 1 #initializes a loop variable

        while j <= k: #loops while j is less than or equal to the number of boxes
            temp = 1/(math.factorial(j)) #sets the temp variable equal to the value
            temporary = 0 #sets another temp variable equal to 0

            for i in range(j - 1): #loops through the range of values up to j - 1
                temporary += ((-1) ** i) * (math.factorial(j) / (math.factorial(j - i) * math.factorial(i))) * ((j - i) ** n) #formula to find the number of ways to sort distinguishable objects into indistinguishable boxes

            ans += temp * temporary #multiplies the sum of temporary to the previously found temp variable and sums it
            j += 1 #increments the loop variable

        return math.ceil(ans) #returns the answer

def neither_distinguishable(n, k):
    ans = [] #initialize the answer

    if n < k: #checks to see if the number of objects is less than the number of boxes
        return 1

    else:
        p = [0] * n     # An array to store a partition
        i = 0         # Index of last element in a partition
        p[i] = n     # Initialize first partition
                    # as number itself
    
        # This loop first prints current partition,
        # then generates next partition.The loop
        # stops when the current partition has all 1s
        while True:
            
                # print current partition
                ans.append(p)
    
                # Generate next partition
    
                # Find the rightmost non-one value in p[].
                # Also, update the rem_val so that we know
                # how much value can be accommodated
                rem_val = 0
                while i >= 0 and p[i] == 1:
                    rem_val += p[i]
                    i -= 1

                temp = []

                for j in p:
                    if j != 0:
                        temp.append(j)
    
                # if i < 0, all the values are 1 so
                # there are no more partitions
                if i < 0 or len(temp) > k:
                    return len(ans) - 1
    
                # Decrease the p[i] found above
                # and adjust the rem_val
                p[i] -= 1
                rem_val += 1
    
                # If rem_val is more, then the sorted
                # order is violated. Divide rem_val in
                # different values of size p[i] and copy
                # these values at different positions after p[i]
                while rem_val > p[i]:
                    p[i + 1] = p[i]
                    rem_val = rem_val - p[i]
                    i += 1
    
                # Copy rem_val to next position
                # and increment position
                p[i + 1] = rem_val
                i += 1

def main():
    print(both_distinguishable(52, 4, 5))
    print(both_distinguishable(40, 4, 10))
    print(boxes_distinguishable(10, 8))
    print(boxes_distinguishable(12, 6))
    print(objects_distinguishable(4, 3))
    print(objects_distinguishable(5, 4))
    print(neither_distinguishable(6, 4))
    print(neither_distinguishable(5, 3))

if __name__ == '__main__':
    main()