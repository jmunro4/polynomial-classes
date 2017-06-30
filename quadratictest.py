#####################################
# quadratictest.py
# Jonathan Munro
#####################################

'''Prints statements that tests every aspect of the Quadratic class and aspects from the Polynomial class for the user to review.'''
from quadratic import *
from polynomial import *

def main():
    '''prints the statements'''
    #sets up different Quadratics and a Polynomial
    quad1 = Quadratic(-1, 2, 1) 
    quad2 = Quadratic(5, 60, 2) #sqrt(-num)
    quad3 = Quadratic(3, 0, 7)
    quad4 = Quadratic(6, 3, 0) #has no x2, roots should return None
    poly1 = Polynomial([1, 3, 5, 6, 8])

    #tests the getDegree
    print('\n---testing getDegree---\n')
    print('2 2 2 1 :')
    print(quad1.getDegree(), quad2.getDegree(), quad3.getDegree(), quad4.getDegree())
    
    #tests the getCoefficient with different powers
    print('\n---testing getCoefficient---\n')
    print('2 :', quad1.getCoefficient(1))
    print('0 :', quad4.getCoefficient(2))

    #test the printing, examples above the print statement for easy review
    print('\n---testing __str__---\n')
    print('(x^2 + 2x - 1)', '(2x^2 + 60x + 5)', '(7x^2 + 3)', '(3x + 6) :')
    print(quad1, quad2, quad3, quad4)

    #test the addition of Quadratics and the addition of a Polynomial and Quadratic
    print('\n---testing __add__---\n')
    print(quad1,'+',quad2,'=\n(3x^2 + 62x + 4) =')
    print(quad1+quad2)
    print(quad3,'+',poly1,'=\n(8x^4 + 6x^3 + 12x^2 + 3x + 4) =')
    print(quad3+poly1)

    #test the subtraction of Quadratics and the subtraction of a Polynomial and Quadratic
    print('\n---testing __sub__---\n')
    print(quad1,'-',quad2,'=\n(- x^2 - 58x - 6) =')
    print(quad1-quad2)
    print(poly1,'-',quad3,'=\n(8x^4 + 6x^3 - 2x^2 + 3x - 2) =')
    print(poly1-quad3)

    #test the multiplication between Quadratics and between Quadratics and Polynomials
    print('\n---testing __mul__---\n')
    print(quad1,'*',quad2,'=\n(2x^4 + 64x^3 + 123x^2 - 50x - 5) =')
    print(quad1*quad2)
    print(poly1,'*',quad3,'=\n(56x^6 + 42x^5 + 59x^4 + 39x^3 + 22x^2 + 9x + 3)')
    print(poly1*quad3)

    #test the equality method, between same and different Quadratics and with a Polynomial
    print('\n---testing __eq__---\n')
    print(quad1,'==',quad1,quad1==quad1)
    print(quad2,'==',quad3,quad2==quad3)
    print(quad4,'==',poly1,quad4==poly1)

    #test the getRoot and eval methods. First finds the roots of the quadratic
    #if they exist and aren't imaginary they are passed to eval
    #should return 0 or near zero due to rounding concerns
    print('\n---testing getRoots & eval---\n')
    roots1 = quad1.getRoots()    
    print(quad1, roots1)
    print(quad1,'@ getRoots', quad1.eval(roots1[0]), quad1.eval(roots1[1]))
    print('first root number does not give perfect zero due to rounding')
    roots2 = quad2.getRoots()
    print(quad2, roots2)
    print(quad2,'@ getRoots', quad2.eval(roots2[0]), quad2.eval(roots2[1]))
    print('first root number does not give perfect zero due to rounding')
    roots3 = quad3.getRoots()
    print(quad3, roots3)
    print(quad3,'@ 5', quad3.eval(5),'(178)') #couldn't put in imaginary roots
    roots4 = quad4.getRoots()
    print(quad4, roots4)
    print(quad4,'@ 3', quad4.eval(3), '(15)') #no roots to put in

main()
