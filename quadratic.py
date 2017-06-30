################################
# quadratic.py
# Jonathan Munro
################################
'''Creates a Quadratic class from three numbers, the coefficients of the quadratic'''
from polynomial import *
import cmath

class Quadratic(Polynomial):
    '''Creates a Quadratic type object from three numbers that are the coefficients'''
    def __init__(self, x0, x1, x2):
        #creates a list with the coefficients so it can properly inherent from the Polynomial class
        coefficients = [x0, x1, x2]
        super().__init__(coefficients)
        #sets up the coefficients
        self.__x2 = x2
        self.__x1 = x1
        self.__x0 = x0

    def getRoots(self):
        '''returns the roots or zeros of the Quadratic'''
        #assigns to variable used int the quadratic equation for ease
        a = self.__x2
        b = self.__x1
        c = self.__x0

        #returns None so it doesn't divide by 0
        if a == 0:
            return None
        else:
            #uses cmath to take care of the negative under the square root
            if b**2 < (4*a*c):
                one = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
                two = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
            #to avoid the unnecessary imaginary number from cmath
            else:
                one = (-b + ((b**2 - 4*a*c)**.5))/(2*a)
                two = (-b - ((b**2 - 4*a*c)**.5))/(2*a)
        #returns a tuple
        return (one, two)
