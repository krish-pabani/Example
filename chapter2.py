# Strings
#concatenation
first_name = "Virat"
last_name = "Kohli"
full_name = first_name + " " + last_name
print(full_name)

#print(first_name + 3)  error because string can't concate with number
# for that convert number into string

print(first_name + str(3))
# or 
print(first_name + "3")

# we can use * to have that name multiple times
print(first_name * 3)

#user input
# input function always takes input as string can see in age input 
name = input("Type your name: ")
print("Hello "+ name)
age = input("Type your age :")
print("Your age is "+ age)

#as input always takes input as string
no_1 = input('Enter first number') #4
no_2 = input('Enter second number') #4
total = no_1 + no_2 #44
print('total' + total) #total44

# to convert string in int or reverse 
no_1 = int(input('Enter first number')) #4 converting input string in int 
no_2 = int(input('Enter second number')) #4
total = no_1 + no_2 #8
print('total' + str(total)) #total8 converting int in string

#str
#4---->"4"

# int
# "4"---->4

# float
# "4"---->4.0

# int and float can be add but string cannot be add with int and float

# How to declare multiple variable together
name, age = "John", 19
print(name)
print(age)
x=y=z=1
print(x+y+z)

# How to declare multiple inputs together
name, age = input("Enter your name and age ").split()
print(name)
print(age)
#or inside split , to have input separator while inputing your values
name, age = input("Enter your name and age ").split(",") #in console if you input space before any string then it will also consider space in that string  
print(name)
print(age)

#string fformatting 
name, age = "John",19
print("Hello " + name + " your age is " + str(age))
print('Hello {} your age is {}'.format(name, age)) #python 3
print(f'Hello {name} your age is {age}') #python 3.6, dont forget to write f before string

#using string you can also perform any operation
print(f'Hello {name} your age is {age + 5} {5-9}')

#Exercise 
x,y,z = input("Enter number X, Y and Z: ").split()
print(f"Average of the X, Y & Z is: {(int(x)+int(y)+int(z))/3}")

# String Indexing
language = "python"
#positions
# p = 0 , -6
# y = 1 , -5
# t = 2 , -4
# h = 3 , -3
# o = 4 , -2
# n = 5 , -1
print(language[2])
print(language[-4])

# String Slicing / Selecting sub squences
language = "python"
# Syntax = print(var[ start argument : stop argument (if want to stop at 2 position then write 3) ])
print(language[0:2]) # can also use negative indexes as arguments
print(language[:])
print(language[2:])
print(language[:3])

# Step argument
print("Johnesh"[0:5:1])
print("Johnesh"[0:5:2])
print("Johnesh"[0::2])
print("Johnesh"[0:5:3])
print("Johnesh"[::2])
print("Johnesh"[5::-1])
print("Johnesh"[-1::-1]) 
print("Johnesh"[::-1]) # will have same output as above

#Exercise
name = input("Enter your name: ")
print(f"Reverse of {name} is {name[-1::-1]}")

# String Methods
name = "JohneShM  MehNaDia"
#len() function : will also count spaces
print(len(name))
#or
length = len(name)
print(length)
#lower() method
print(name.lower())
#upper() method
print(name.upper())
#title() method
print(name.title())
#count() method
print(name.count("h"))

#Exercise
name, singleCharacter = input("Enter your name and one any single character").split(",")
print(len(name))
print(name.lower().count(singleCharacter.lower()))# To make case insensitive

#Strip Method
name = "    Harshit    "
name2 = "   Har   shit   "
dots = "............."
#lstrip method
print(name+dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)
print(name2.strip() + dots) # will not remove space in between the words
print(name2.replace(" ","")) # will replace space with no spaces

# find and replace methods
string = "She is beautiful and she is good dancer"
print(string.replace("is","was"))
print(string.replace("is","was",1))
print(string.replace("is","was",2))

print(string.find("is")) # will show index of start letter of word you want to find
print(string.find("is",5)) # here index is from where you want to start search that word

#center method
name = "harshit"
#**harshit**
print(name.center(11,"*"))
print(name.center(10,"*"))
name2 = input("Enter your name: ")
print(name2.center(len(name2) + 8,"*")) #to add 4 * on each side of name that user inputs

#Strings are immutable
#Once string is defined it can't change any character of it
string = "string"
#string[1] = "T" # will show an error
print(string.replace("t","T")) # will replace and print the output but in string will not change, see next line output
print(string)  
newString = string.replace("t","T") 
print(newString)

#assignment operators
name = "Jhonesh"
name = name + "it"
name += "it"
print(name)
age = 19
age *= 2
print(age)
age -= 2
print(age)
age /= 2
print(age)
