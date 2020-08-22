# # tuples data  structure
# # tuple can store any data type
# # most important tuples are immutable, once tuple is created you can't update
# # data inside tuple
# example = ("one","two",1,3,1)
# #no append no insert no pop no remove
# #tuples are faster

# # methods used in tuples
# # count, index
# print(example.count(1))
# print(example.index("two"))
# # len function
# print(len(example))
# # slicing
# print(example[:3])
# # #below code will show an error
# # example[0] = 1
# # print(example)

# #looping in tuples ---- for and while both can be used
# mixed = (1,2,3,4.0)
# for i in mixed:
#     print(i)

# #tuple with one element
# num = (1) # not a tuple
# mixed = (1,) # tuple - if you want only one element in tuple you must write comma after the element inside the parenthesis
# words = ('word1')
# print(type(num))
# print(type(mixed))
# print(type(words))

# #tuple without parenthesis
# guitar = 'xyz','asd','ewg' # tuple
# print(type(guitar))

# #tuple unpacking
# guitarists = ('NJ','FY','TK')
# guitarist1, guitarist2, guitarist3 = (guitarists) # no. of variable declared should be same as the no. of elements in tuple, if it will be not equal then code will show error 
# print(guitarist3)
# # list inside tuple
# favorites = ('SK',['abc','efg'],['mng','qwe'])
# favorites[1].pop()
# favorites[1].append("we made it")
# print(favorites)

# # some functions that you can use with tuples
# #min , max, sum
# mixed = (1,2,3,4.0)
# print(min(mixed))
# print(max(mixed))
# print(sum(mixed))

# # function returning two values
# def func(int1, int2):
#     add = int1 + int2
#     multiply = int1 * int2
#     return add, multiply

# print(func(2,3)) # will return tuple
# add, multiply = func(2,3)
# print(add)
# print(multiply)

# # nums = tuple(range(1,11))
# # print(nums)
# # tuple to list
# nums = list((1,2,3,4,5,6,7,8,9,10))
# print(nums)
# print(type(nums))
# # tuple to string
# nums = str((1,2,3,4,5,6,7,8,9,10))
# print(type(nums))

 

