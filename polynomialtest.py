#########################
# polynomial.py
# part of homework 1 problem 1
# Jonathan Munro
#########################
'''The module contains the Polynomial class. This takes a list of coefficients and creates a Polynomial object.'''

class Polynomial:
    '''This class creates a Polynomial object. It takes a list of coefficients'''
    def __init__(self, coefficients):
        '''The constructor method for Polynomial'''
        self.__list = coefficients[:]
        copy = coefficients[:]
        #takes out extra zeros to find the real degree of the polynomial
        while copy[-1] == 0:
            copy.pop()
        self.__degree = len(copy) - 1

    def getDegree(self):
        '''Returns the degree of the Polynomial'''
        return self.__degree

    def getCoefficient(self, power):
        '''Returns the coefficient associated with the given power'''
        if power > self.getDegree():
            #this covers anything that might not be in self.__list
            return 0
        else:
            return self.__list[power]

    def __str__(self):
        '''Overrides string to properly print the Polynomial'''
        string = ')'
        #goes through for each term in the polynomial
        for i in range(self.getDegree() + 1):
            #sets up the correct sign and stores the coefficient
            if self.getCoefficient(i) > 0:
                sign = ' + '
                coef = str(self.getCoefficient(i))
            elif self.getCoefficient(i) < 0:
                sign = ' - '
                coef = str(self.getCoefficient(i))[1:]
            else:
                sign = ''
            
            #starts making the terms, they won't appear if they are 0
            if self.getCoefficient(i) != 0:
                #x^0 is 1 so it should just be the coefficient
                if i == 0:
                    string = sign + coef + string
                #x^1 is x so there won't be a ^
                elif i == 1:
                    #if the coefficent is 1 it shouldn't appear
                    if self.getCoefficient(i) == 1 or self.getCoefficient(i) == -1:
                        string = sign + 'x' + string
                    else:
                        string = sign + coef + 'x' + string
                #for all other terms
                else:
                    #so the 1's don't show
                    if self.getCoefficient(i) == 1 or self.getCoefficient(i) == -1:
                        string = sign + 'x^' + str(i) + string
                    else:
                        string = sign + coef + 'x^' + str(i) + string
        #if the 1st term is a negative it keeps the sign
        if self.getCoefficient(self.getDegree()) < 0:
            return '(' + string[1:]
        #otherwise it cuts it out
        else:
            return '(' + string[3:]

    def __add__(self, other):
        '''Overrides add to work with Polynomials'''
        newPoly = []
        #easy way to tell which is longer and how many extra terms there will be
        diff = self.getDegree() - other.getDegree()
        #means the other polynomial will have more terms, diff * -1 for ease later
        if diff < 0:
            longer = other
            diff *= -1
        #the self polynomial will have more terms
        else:
            longer = self

        #goes through each term in the longer polynomial so coefficients don't get dropped
        for i in range(longer.getDegree()+1):
            #while there are two coefficients to add
            if i <= longer.getDegree() - diff:
                newPoly.append(self.getCoefficient(i) + other.getCoefficient(i))
            #adds on the coefficients that would be +0
            else:
                newPoly.append(longer.getCoefficient(i))

        return Polynomial(newPoly)

    def __sub__(self, other):
        '''Overrides subtract to work with Polynomials'''
        newPoly = []
        #easy way to tell which is longer and how many extra terms there will be
        diff = self.getDegree() - other.getDegree()
        #the other polynomial will have more terms, diff *-1 for ease later
        if diff < 0:
            longer = other
            diff *= -1
        #the self polynomial has more terms
        else:
            longer = self

        #goes through every term in the longer polynomial so no info is lost
        for i in range(longer.getDegree()+1):
            #while there are two coefficients to subtract
            if i <= longer.getDegree() - diff:
                newPoly.append(self.getCoefficient(i) - other.getCoefficient(i))
            #the extra coefficients from the longer polynomial
            else:
                #if the longer is the self nothing changes
                if longer == self:
                    newPoly.append(longer.getCoefficient(i))
                #if the longer is the other it has to be 0 - other, because its self - other
                else:
                    newPoly.append(0-longer.getCoefficient(i))
                
        return Polynomial(newPoly)

    def __mul__(self, other):
        '''Overrides multiply to work with Polynomials'''
        mulDict = {}
        newPoly = []
        #goes through as each coefficient is multiplied by the other
        for i in range(self.getDegree()+1):
            for j in range(other.getDegree()+1):
                #i+j is recorded as the power with the coefficient
                #if the power already has a coefficient the new coefficient is added
                if i+j in mulDict:
                    mulDict[i+j]= (self.getCoefficient(i)*other.getCoefficient(j)) + mulDict[i+j]
                #if it doesn't exist it is created
                else:
                    mulDict[i+j]=self.getCoefficient(i)*other.getCoefficient(j)

        #goes through for each power and creates a list of coefficients to create a new polynomial
        for k in range((self.getDegree()+other.getDegree())+1):
            newPoly.append(mulDict[k])

        return Polynomial(newPoly)

    def __eq__(self, other):
        '''Overrides equal to compare Polynomials'''
        #its spliced to ignore the potential zeros before the first significant term
        return str(self)[:self.getDegree()] == str(other)[:other.getDegree()]

    def eval(self, value):
        '''Evaluates the Polynomial for the given value'''
        val = 0
        #goes through each term in the polynomial and plugs in the value
        for i in range(self.getDegree() + 1):
            val += (value ** i) * self.getCoefficient(i)
        return val
