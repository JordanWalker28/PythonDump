# <--- Single Line comment

"""
    This is a multi line comment
"""

#Generic Print Statement
print("Hello")
print("My name is")

#new line
print("\n")

#system sound
print("\a")

#print a statement multiple times
print("Hello " * 10)

#print calculations
print(1+2+3)

#Can use single or double quotes
print("Hello Jordan")
print('Hello')

#Can use quotes between character i.e
#If you start with one you muse end with one though
print("Jordan's tall")
print('Jordan has been known to "program" late into the night')

#combining escape characters
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting"')


#concat
print("Jordans" + " quick" + " guide")

#print variables
greeting = "Hello "
name = "Jordan"
print(greeting + name)

#multi line variable strings

anotherSplitString = """This string
has been split over
several lines"""
print(anotherSplitString)

# " " <--- space
# "" <--- empty

#tabs
tabString = "1\t2\t3\t4\t5\t"
print(tabString)

#getting specific characters
team = "Manchester City"
print(team)
print(team[0])
print(team[-1])

#parts of a string
print(team[0:10]) #range from the first character till the specified range
print(team[:10]) #shorthand for previous 
print(team[11:]) #everything after the 11th character
print(team[0:10:2]) #every second character in the range of the first 10 characters
print(team[-5:-1]) #everything from the reverse of the string

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3]) #useful for printing certain aspects of a formulated string

#check if substring x is part of string y
var1 = "today"
print("day" in var1) #Return True
print("can" in "cannot") #Return True
print("dope" in "hello") #Returns False

#numbers and strings
age = 27
#print("My age is " + age + " years") <-- causes error
#alternative
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31,
        "January", "March", "May", "July", "August", "October", "December"))

for i in range (1,12):
    print("{0} squared is {1} and cubed is {2}".format(i, i*i, i**i))

print("Pi is approximatley {0}".format(22/7))
print("Pi is approximatley {0:12.50}".format(22/7))
