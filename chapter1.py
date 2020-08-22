print("Hello World")
print('Hello World')
# double quotes "" can be used in single quotes and vice versa
# but single can't use inside single and same double can't use inside double
print("Hello 'world' World")
print('Hello "world" World')
# Escape Sequence       Meaning
#       \'              single quote 
#       \"              double
#       \\              backslash
#       \n              new line
#       \t              tab     
#       \b              backspace
# to use single inside single and double inside double
# put backslash \ before the quotes
print('I\'m Krish')
print('line A\nline B\nline C')
print('line A\tline B\tline C')
print("This is backslash \\")
print("This is backslash \\\\")
print('Hell\bpo')
print('Hell\b\b\by')
print('Line A \\n Line B')
# \" \'
print('\\\" \\\'')
# Exercise 
print("This is \\\\ double backslash")
print("These are /\\/\\/\\/\\/\\ mountains")
print("he is\t awesome")
print("\\\" \\n \\t \\\'")

# to treat all escape sequences as text put r before opening quotes of string in parenthesis
print(r"\n \t \\ \b \' \" ")

# how to print emoji
# https://unicode.org/emoji/charts/full-emoji-list.html
# copy unicode of emoji you like to print and add 000 in place of + in unicode 

print("\U0001F618")
print("\U0001F608")

# python as a calculator
# + - * /(float division) //(integer division) %(modulo) **(exponent)

print(2+3*6)
print(2/4)
print(4/2)
print(2//4)
print(4//2)
print(2**3)
print(2**0.5)
print(round(2**0.5, 4)) # round the answer in 4 decimal values

# precendence rule 
# OPERATORS           PRECEDENCE AND ASSOCIATIVITY RULE
# Parenthese            highest
# Exponent              Right To Left
# *,/,//,%              Left To Right
# +,-                   Left To Right
print(2-3+1)
# -1 + 1  L to R
print(2**2**3)
# 2**8  R to L

#VARIABLES
number1 = 2
print(number1)
number1 = 5
print(number1)

name = "John"
print(name)
name = 123
print(name)

# Rules of Variable
# variable name should not start with number 
# can start with any letter or _ underscore
# can't use special symbols in variable name

#Conventions for variable naming
user_first_name = "John" # snake case writing recommend for python coding
userFirstName = "John"   # camel case writing 

