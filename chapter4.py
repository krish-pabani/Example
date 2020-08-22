# #functions
# name = "Johnesh"
# print(len(name)) #here len() is a function

# def add_two(a,b):
#     return a+b

# total = add_two(5,4)
# print(total)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# total = add_two(a,b)
# print(total)

# fn = input("Enter first name: ")
# sn = input("Enter second name: ")
# print(add_two(fn,sn))

# #return vs print
# def add_three(a,b,c):
#     # print(a+b+c) # we can also use print inside function but return is better for functions if there is no print statement
#     return a+b+c 

# add_three(5,5,5)

# #functions practice
# def last_char(name):
#     return name[-1]

# print(last_char("Johnesh"))

# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     else:
#         return "odd"
# num = int(input("Input any number: "))
# print(odd_even(num))



# def is_even(num):
#     if num%2 == 0:
#         return True
#     return False
# print(is_even(10))
# #OR above function's short method is mentioned below
# def is_even(num):
#     return num%2 == 0

# print(is_even(9))

# def song():
#     return "Hohohoh"

# print(song())

# #exercise
# def greater_num(a,b):
#     if int(a)>int(b):
#         return "A is greater"
#     else:
#         return "B is greater"

# num1, num2 = input("Enter two number num1 & num2: ").split(" ")
# print(greater_num(num1,num2))
# #OR
# def greater_num(a,b):
#     if a > b:
#         return "A is greater"
#     else:
#         return "B is greater"

# num1 = int(input("Enter number num1: "))
# num2 = int(input("Enter number num2: "))
# bigger = greater_num(num1,num2)
# print(f"{bigger} is greater")

# def greater_num(a,b,c):
#     if a > b and a > c:
#             return "first number is greater"   
#     elif b > a and b > c:
#             return "second number is greater"
#     else:    
#             return "third number is greater"

# num1 = int(input("Enter first numbers: "))
# num2 = int(input("Enter second numbers: "))
# num3 = int(input("Enter third numbers: "))
# print(greater_num(num1,num2,num3))

# #function inside function
# def greater(a,b):
#     if a > b:
#         return a
#     return b

# def greatest(a,b,c):
#     # bigger = greater(a,b)
#     # return greater(bigger,c) 
#     return greater(greater(a,b),c) 

# print(greatest(10,200,30))

# #Exercise

# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False

# print(is_palindrome("RaaR"))
# print(is_palindrome("RaaRaa"))
# #OR
# def is_palindrome(word):
#     return word == word[::-1]

# print(is_palindrome("RaaR"))
# print(is_palindrome("RaaRaa"))

# #fibonacci series
# def fibona(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n == 2:
#         print(a, b)
#     else:
#         print(a,b, end = " ")
#         for i in range(n-2):
#             c = a + b
#             a = b
#             b = c
#             print(b, end = " ")

# n = int(input("Enter number: "))
# fibona(n)

# #default parameters
# def user(fs, ls, age = 12):
#     print(f"your first name is {fs}")
#     print(f"your last name is {ls}")
#     print(f"your age is {age}")

# user("Krish","pabani")

# def user(fs, ls, age = None):
#     print(f"your first name is {fs}")
#     print(f"your last name is {ls}")
#     print(f"your age is {age}")

# user("Krish","pabani")
#  # below code will show an eror because only last paramaters we can make default, make age also as default error will be gone
# def user(fs, ls = "unknown", age):
#     print(f"your first name is {fs}")
#     print(f"your last name is {ls}")
#     print(f"your age is {age}")

# user("Krish",23)

#scope 
# below code will show an error
# def func():
#     x=7
#     return x

# def func2():
#     print(x)

# func2()
#error
# def func():
#     x=7 #local variable
#     return x
# print(x)

# x = 5 #global variable
# def func():
#     x = 7 #local variable, will have scope inside this function only
#     return x

# print(func())
# print(x) 

# #to use global as local
# x = 5 #global variable
# def func():
#     global x
#     x = 7 
#     return x

# print(func())
# print(x) 