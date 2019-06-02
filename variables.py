__author__ = "Jordan"

#create an object in memory
name = "Jordan"

"""

Good practice is that a variable can start with underscore or letter but not number

"""

_myName = "Jordan"
myName = "Jordan"

"""

Two variables with the same spelling but different upper and lowercase letters
are treated as different variables

"""

random = "Tree"
Random = "Cone"
ranDOM = "Hairy" #This would be considered bad practice though

print(random + " " + Random + " " + ranDOM)

age = 27

#print(_myName + " is " + age) will cause an error i.e. int cant be in the String

#Workarounds include: 
print(_myName + " is " + str(age))
print(_myName + " is" , age)

#Datatypes

a = 12 #number/integer
b = 2.05 #decimal/floating point
c = "Hello" #String
d = True #Boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Mathematics
ex1 = 12
ex2 = 3
print(ex1 + ex2) #Add
print(ex1 - ex2) #Minus
print(ex1 * ex2) #Times
print(ex1 / ex2) #Divide (with floating point)
print(ex1 // ex2) #Divide with integer division i.e. 15 // 7 = 2
print(ex1 % ex2) #Modulo

#Order of operations
print(ex1 + ex2 / 3 - 4 * 12)
#returns -35.0
#works in the format BODMAS/BIDMAS

#Using brackets to formulate the correct order
print((((ex1 + ex2) / 3) -4) *12)
#returns 12.0

#for loop
for i in range (1, ex1//ex2):
    print(i)

