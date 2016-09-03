#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

'''
answer to Google's 2004 billboard riddle:
first 10-digit prime found in consecutive digits of e
'''

import decimal
import operator
import functools
from math import sqrt

# generate e with precision 150
decimal.getcontext().prec = 150
# complete e number
e = decimal.Decimal(1).exp().to_eng_string()
# only digits after comma
e_digits = e[2:]

# prime checker function
def isPrime(n):
    if n == 2:
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2)) and n

# find first prime number
for i in range(len(e_digits)):
    p = functools.reduce(operator.add, e_digits[i:i+10])
    p = int(p)
    p = isPrime(p)
    if (p != False and p != True):
        print ("Prime number: %d" % p)
        print ("Digit number: %d" % i)
        break
