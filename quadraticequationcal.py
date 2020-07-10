import matplotlib.pyplot as plt 
import numpy as np

def  my_quard(a : float, b : float, c : float) -> list:
    """Function that solves the quadratic formula

    Args:
        a (float): value for a
        b (float): value for b
        c (float): value for c

    Returns:
        set: return value for root1 and root2
    """

    x1 = (-b + (b**2 -(4*a*c))**0.5)/2*a
    x2 = (-b - (b**2 -(4*a*c))**0.5)/2*a
    return (x1, x2)

def plotty(x: float, y: float, z: float) -> None:
    """this will plot the graph

    Args:
        x (float): value for a
        y (float): value for b
        z (float): value for c
    """
    m = np.linspace(-10, 10, 1000)
    n = [x*(space**2) + (y*space) + z for space in m]
    plt.plot(m, n)
    plt.show()
    



def Execute():
    
    print("\nThis is the quadratic equation solver")    
    while True:
        try:
            a = float(input("\nPlease enter a value for 'a': "))
            if a == 0:
                continue
            b = float(input("Please enter a value for 'b': "))
            c = float(input("Please enter a value for 'c': "))
            break
        except:
            print("One or two inputs are not right")
        

    root1, root2 = my_quard(a, b, c)
    print("\nThe roots are {} and {}".format(root1, root2))
    print("See graph output")
    plotty(a, b, c)



    
