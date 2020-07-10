""" imports both the gauss jordan and the quadratic codes as
    python packages
"""

import quadraticequationcal as quad
import gauss_jordancal as gd

if __name__ == "__main__":
    # Display a welcome note and give the instructions
    print ("\nHEY THERE, WELCOME\n")
    print ("\tThis calculator solves for the roots of a quadratic\
        \n\tformula in the form: ax^2+bx+c=0 \
            \n\twhere a, b, and c are the coefficients\
            \n\tAlso it solves simultaneous equations")
    print ("\nPlease enter \n\t1 for Quardratic equation\n\t2 for Simultaneous equations")

    """This while loop allows a user to input the equation
        they want to solve.
    """
    while True:
        try:
            selection = int(input())
            #this if block executes the quadratic equation when user input is 1
            if selection == 1:
                quad.Execute()
                break
            #this block executes the gauss-jordan equation when user input is  2
            elif selection == 2:
                gd.Execute()
                break
            #this block is executed when the user input is any \
            # integer either than 1 and 2
            else:
                print("please enter a valid number [1 or 2]")
                continue
        #this block takes care of inputs that are strings
        except:
            print("Enter a number\nPlease enter a valid number [1 or 2]")
        



    

