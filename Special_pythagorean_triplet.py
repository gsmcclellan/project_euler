"""Greg McClellan
   Created: 8/4/13
   Last Edited: 8/4/13

   Program will find one unique Pythagorean triplet for which a + b + c = 100
"""

#Given: a < b < c
#Given: a**2 + b**2 == c**2
#Given: a + b + c == 1000

from math import sqrt

class Triplet(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = sqrt(a**2 + b**2)

    def __repr__(self):
        return "(%i, %i, %i)" %(self.a, self.b, self.c)

    def check_triplet(self):
        #Returns true if the 3 values make up a pythagorean triplet of integers
        if(self.c == int(self.c)):
            return True
        else:
            return False

    def product(self):
        #returns product of a, b, and c
        return int(self.a * self.b * self.c)

    
def find_triplet():
    #Finds the special triplet and returns as class Triplet
    a = 1

    for a in range(1, 333): #upper limit for a
        
        for b in range(a, 500): #upper limit for b
            c = 1000 - a - b
            triplet = Triplet(a, b)
            if(triplet.check_triplet()):
                print(triplet)
                if(triplet.c == c):
                    return triplet

    return False

triplet = find_triplet()
print(triplet)
print(triplet.product())

