#Link --> https://www.codewars.com/kata/66939247fc2af275cd8a82d3

#Instructions:
#Given a non-degenerate triangle with lengths a, b, and c, return 
# 1) the radius of a circle inscribed in the triangle (r) 
# 2) the radius of a circle circumscribed on the triangle (R)

# Examples:
# radii(3, 4, 5) = (1, 2.5)                                   (r = 1, right triangle, thales theorem, so R = 5 / 2 = 2.5)
# radii(1, 1, 1) = (sqrt(3) / 6, sqrt(3) / 3)
# radii(2, 1, 2) = (0.3872983346207417, 1.032795558988644)    (maths, blah blah blah)

import math 

def radii(a, b, c):
    s= (a+b+c)/2
    K = math.sqrt(s*(s-a)*(s-b)*(s-c))
    r = K / s
    R = (a*b*c)/(4*K)
    return r,R

#Explaination
#Radius of Circumscribed Circle (𝑅) = abc/4K
#Radius of Inscribed Circle (r) = K/s

# s -- > semi-perimeter of a triangle
# s = (a+b+c) /2
# K --> Area of Triangle using Herons Formula
# K = sqrt(s*(s-a)*(s-b)*(s-c))
