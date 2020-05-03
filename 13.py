import math #add library 'math'

a = int(input('One Side ')) #input Side
b = int(input('Two Side '))
c = int(input('Three Side '))

p = (a + b + c) / 2 # semi-perimeter

temp1 = p * (p - a) * (p - b) * (p - c) #calculates the area
S = math.sqrt(temp1)

print("Reddy ", S)











