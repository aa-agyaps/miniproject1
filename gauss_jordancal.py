import numpy as np
""" imports the necessary library
"""

def gauss(testing_matrix):
    """ Function that solves argumented matrices using
        the Gauss-Jordan Elimination method

        Arg:
        testing_matrix: least of any matrix

        Returns:
        testing_matrix: values of all coefficients in the equations

    """
    
    number_of_equations = len(testing_matrix) 
    number_of_columns = number_of_equations+1   

    for row in range(number_of_equations):   
        constant = testing_matrix[row][row] #this is because we are looking for the coefficient of the diagonals
        
        #this part does the division for a particular row
        for column in range(number_of_columns): 
            testing_matrix[row][column] = testing_matrix[row][column]/constant
      
        #this part does the subtraction of other rows
        for K in range (number_of_equations):
            if K != row:
                D = testing_matrix[K][row]  #this picks the coefficient of the kth row and the rowth column
                
                #this does the subtraction of each item 
                for M in range(number_of_columns):
                    testing_matrix[K][M] = testing_matrix[K][M] - (testing_matrix[row][M]*D)
        swap(testing_matrix)
    return(testing_matrix)
    
def enterInputs():
    """Function allows user to input all coefficients of the variables
        in the simultaneous equation

        Returns:
        a : augumented matrix of all the coefficients 
    """
    n = int(input("How many variables are in the equation?\n\t"))
    a = np.zeros((n, n+1)) # creats an augumented matrix made up zeros
   
    #puts all inputed variables in matrix a
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input('enter the value in the augmentd matrix row '+str(i+1)+', column '+ str(j+1)+" --> "))
    return a

def swap(mySwapMatrix):
    """ Function that checks if there any zeros
        in the leading diagonal of the augumented matrix(a)
        and goes ahead to swap rows to eliminate zero-diagonals
    """
    myCount = 0
    t = 0
    #this while loop swaps zero diagonals
    while t<len(mySwapMatrix)-1:
        swap1 = [] #selects current row as swap1 for the current iteration
        for item in mySwapMatrix[t]:
            swap1.append(item)                
        swap2 = mySwapMatrix[t + 1]
        if mySwapMatrix[t][t] == 0:
            mySwapMatrix[t] = swap2
            mySwapMatrix[t+1] = swap1
        myCount = myCount+1
        t = t+1
        if myCount == len(mySwapMatrix):
            break
    return(mySwapMatrix)
def Execute():
    """Function that executes the code
    """
    #Displays a welcome notes
    print("\nThis is the simultaneous equation solver")
    MyMatrix = enterInputs()

    newMatrix= swap(MyMatrix)

    answers = gauss(newMatrix)
    for i in range(len(answers)):
        print ('X%d = %0.2f' %(i+1, answers[i][-1]), end = '\t')

