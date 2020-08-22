# * operator
# def total(a,b):
#     return a+b

# print(total(3,4))
# # print(total(3,4,5,6)) # error because argument accepts only 2 values

# # using * we can add as many as arguments
# def total(*args): # * will change all arguments in tuples # write args with * according to convention
#     print(args)
#     print(type(args))
#     sum = 0
#     for num in args:
#         sum += num
#     print(sum)
# total(3,4,5,6,2)

# # *args with normal parameter
# def multiply_nums(num, *args): # *args should always be after normal parameter 
#     multiply = 1
#     print(num)
#     print(args)
#     for i in args:
#         multiply *= i
#     print(multiply)

# multiply_nums(2,2,3,4)

# # how to define *args as argument
# # we e define function it has parameter
# # when we call that function it has argument
# def multiply_nums(*args):
#     multiply = 1
#     print(args)
#     for i in args:
#         multiply *= i
#     print(multiply)

# nums = [2,3,4] #OR as tuple (2,3,4)
# multiply_nums(*nums) # unpack

# #Exercise
# def function(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "You didn't pass any args"


# nums = [1,2,3]
# number = int(input("Enter number:"))
# print(function(number,*nums))

# kwargs (keyword arguments)
# **kwargs (double star operator)

# # kwargs as a parameter
# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# func(fs = "Krish", ls = "Pabani")

# def func(**kwargs):
#    for k, v in kwargs.items():
#        print(f"{k} : {v}")

# func(fs = "Krish", ls = "Pabani")

# def func(name, **kwargs):
#     print(name)
#     print(kwargs)
#     for k, v in kwargs.items():
#        print(f"{k} : {v}")

# func('mohit',fs = "Krish", ls = "Pabani")

# def func(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#        print(f"{k} : {v}")

# #dictionary unpacking
# d = {'name':'Jhon', 'age' : 24}
# func(**d)

# functions with all parameters 
# very important 
# PADK
# parameters, *args, default parameter, **kwargs

# # default parameters
# def func(name = 'unknown', age = 24):
#     print(name)
#     print(age)

# func()
# func('Krish')
# func('Krish', 19)

# def func(name, *args, ls = 'unknown', **kwargs): # parameters, *args, default parameter, **kwargs
#     print(name)
#     print(args)
#     print(ls)
#     print(kwargs)

# func('harshit', 1,2,3, a = 1, b = 2)

# def func(l, **kwargs):
#     if kwargs.get('reverse_str') == True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]

# names = ['Krish','Pabani']
# print(func(names))
# print(func(names, reverse_str = True))