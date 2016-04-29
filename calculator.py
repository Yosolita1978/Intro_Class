import math

def add(num1,num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1,num2):
    return num1/num2

def modulo(num1, num2):
    return num1%num2

def power(num1,num2):
    return math.pow(num1,num2)

def square(num1):
    return math.sqrt(num1)



First = add(4,5) + subtract(9,6)
print First

a = divide(12,2)
second =  subtract(a,60)
print second

c = add(1,2)
c1 = add(c,3)
print c1

d1 = add(1,2)
d = power(d1,2)
print d

e = modulo(3,4) / multiply(9,9)
print e

f = add(3,8)
f1 = multiply(7,f)
print f1

g = add(1,2)
g1 = subtract(g,3)
g2 = add(4,5)
g_Total = multiply(g1,g2)
print g_Total

h1 = add(2,3)
h_total = power(3,h1)
print h_total
 

