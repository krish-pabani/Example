# lambda expressions (anonymous function)
# # uisng function
# def add(a,b):
#     return a+b 
# print(add(2,3))
# print(add) # functions have names

# # using lambda expression
# add2 = lambda a,b : a+b
# print(add2(2,3))
# print(add2) # lambda expressions don't have name
# # used in built in function map, reduce filter which will come in next lecture
# multiply = lambda a,b : a*b
# print(multiply(2,3))
# print(multiply) # lambda expressions don't have name

# def is_even(a):
#     return a%2 == 0 # if else in short form, a%2 == 0 ----> true , false

# print(is_even(2))
# print(is_even(5))

# # now using lambda 
# is_even2 = lambda a : a%2==0
# print(is_even2(2))
# print(is_even2(5))

# # usinf func
# def last_char(s):
#     return s[-1]
# print(last_char('Krish'))
# # using lambda
# last_char = lambda s : s[-1]
# print(last_char('Krish'))

# lambda with if else 
# usinf func
def func(s):
    if len(s) > 5:
        return True
    return False

print(func("KRISHH"))   
# using lambda
func = lambda s : True if len(s)>5 else False
print(func("KRISHH"))   
# usinf func
def func(s):
    return len(s) > 5

print(func("KRISHH"))   
# using lambda
func = lambda s : len(s)>5
print(func("KRISH"))  