###############################################################################
############################# EULER TOOLS #####################################
###############################################################################


###############################################################################
                            # SUITE DE FIBONACCI #
###############################################################################

def fibonacci(N):
    
    """ Returns a fibonacci suite. """
    
    a, b = 1, 1
    suite = list()
    
    for n in range(N-1):
        a, b = b, a+b
        suite.append(a)
        
    return suite


###############################################################################
                            # CRIBLE D'ERATOSTHENE #
###############################################################################

from math import sqrt

def eratosthenes(N):
    
    """ Returns prime numbers below N. """
    
    n_square = int(sqrt(N)) + 1
    crible = dict()

    for i in range(2, N):
        crible[i] = True
    
    for j in range(2, n_square):
        if crible[j] == True:
            for k in range(2*j, N, j):
                crible[k] = False
        
    result = list()
    
    for v in crible:
        if crible[v] == True:
            result.append(v)
    
    return result


###############################################################################
                            # PALINDROMIC NUMBERS #
###############################################################################
                            
def is_palindrome(n):
    
    """ Returns True if n is a palindromic number. """
    
    return str(n) == str(n)[::-1]


###############################################################################
                            # LEAST COMMON MULTIPLE #
###############################################################################

def lcm(numbers):
    
    """ Returns the LCM of two or more numbers (input == list()). """

    N = max(numbers) # In case of numbers in disorder.
    crible = eratosthenes(N)
    multiples = dict()

    for n in numbers:
        factors = dict()
        
        for i in crible:
            if n%i == 0:
                if i not in factors:
                    k = n
                    m = 0
                    while k % i == 0:
                        k = k/i
                        m += 1
                    factors[i] = m
                    multiples[n] = factors
               
    lcm = dict() 
    for k in crible:
        lcm[k] = 0
    
    for multiple in multiples.values():
        for k, v in multiple.items():
            if k in lcm:
                if v >= lcm[k]:
                    lcm[k] = v
    
    r = list()
    for k,v in lcm.items():
        r.append(k**v)
    
    result = 1
    for i in r:
        result *= i
        
    return result


###############################################################################
                            # SUM OF THE SQUARES #
###############################################################################

def sum_of_the_squares(numbers):
    
    """ Returns the sum of the squares of a list of input numbers. """
    
    result = 0
    for i in numbers:
        result += i**2
    
    return result

                            
###############################################################################
                            # SQUARE OF THE SUM #
###############################################################################
                            
def square_of_the_sum(numbers):

    """ Returns the square of the sum of a list of input numbers. """

    N = 0
    for i in numbers:
        N += i
    
    return N**2


###############################################################################
                            # ADJACENT PRODUCT #
###############################################################################

def adjacent_product(n, numbers):

    """ Returns the product of n adjacent numbers. """
    
    temp_result = 1
    result = 0
    
    for i in range(len(numbers)):
        nn = numbers[i:i+n]
        for i in nn:
            temp_result *= i
            if temp_result >= result:
                result = temp_result
        temp_result = 1
    
    return result
