# #data structures
# #lists
# #ordered collections of items
# # you can store anything in lists int, float, string 

# numbers = [1,2,3,4]
# print(numbers)

# words = ["word1" , "word2" , "word3"]
# print(words)

# mixed = [1,2,3,4,"5","6","3.4","john",None]
# print(mixed)

# print(numbers[1])
# print(words[:2])
# print(mixed[-1])

# mixed[1] = "two"
# print(mixed)

# mixed[1:] = ["two","three"]
# print(mixed)

#How to add items to our list
# fruits = ["Orange","Apple"]
# fruits.append("Grapes")
# print(fruits)

# fruits = ["Orange","Apple"]
# fruits.insert(1, "Grapes")
# print(fruits)

# fruits1 = ["Orange","Apple"]
# fruits2 = ["Mango","Grapes"]
# fruits = fruits1+fruits2
# print(fruits)

# fruits1 = ["Orange","Apple"]
# fruits2 = ["Mango","Grapes"]
# fruits1.extend(fruits2)
# print(fruits1)
# print(fruits2)

# #list inside list
# fruits1 = ["Orange","Apple"]
# fruits2 = ["Mango","Grapes"]
# fruits1.append(fruits2)
# print(fruits1)
# print(fruits2)

# #Delete data from lists
# # fruits = ["Orange","Apple","Mango","Grapes"]
# # fruits.pop() #by default deletes last element
# # print(fruits)

# # fruits = ["Orange","Apple","Mango","Grapes"]
# # fruits.pop(1) # deletes particular element
# # print(fruits)

# # fruits = ["Orange","Apple","Mango","Grapes"]
# # del fruits[1] #deletes particular element
# # print(fruits)

# fruits = ["Orange","Apple","Mango","Grapes"]
# fruits.remove('Apple') #delrem etes particular element
# print(fruits)

# # In keyword with list
# fruits = ["Orange","Apple","Mango","Grapes"]
# if "Apple" in fruits:
#     print("Apple is present")
# else:
#     print("Not Present")

# #list methods
# #count
# fruits = ["Orange","Apple","Mango","Grapes","Apple"]
# print(fruits.count("Apple"))
# #sort
# fruits.sort()
# print(fruits)
# number = [3,6,5,1,2]
# number.sort()
# print(number)
# #sorted function
# number = [3,6,5,1,2]
# print(sorted(number))
# print(number)
# # clear
# number = [3,6,5,1,2]
# number.clear()
# print(number)
# #copy
# number = [3,6,5,1,2]
# number_copy = number.copy()
# print(number_copy)

# # is vs equal
# # to compare ----> == & is
# # == values are same then list is same
# # is will check that both the list is at same place in memory or not
# fruits1 = ["Orange","Apple","Mango"]
# fruits2 = ["Orange","Apple","Mango","Grapes","Apple"]
# fruits3 = ["Orange","Apple","Mango"]
# print(fruits1==fruits2) # FALSE : values are not same
# print(fruits1==fruits3) # TRUE : values are same
# print(fruits1 is fruits2) # FALSE : list are not at same place in memory
# print(fruits1 is fruits3) # FALSE : list are not at same place in memory

# #join and split method
# #split
# # user_info = 'Jhonesh 25'.split()
# # print(user_info)
# # user_info = 'Jhonesh,25'.split(",")
# # print(user_info)
# # name, age = 'Jhonesh 25'.split()
# # print(name)
# # print(age)
# #join
# #list to string
# user_info = ['Jhonesh', '25']
# print(','.join(user_info))

# #list vs array
# #array in c, c++, java - stores only one specific data type
# #list in python - stores multiple data type 
# #javascript array = python list
# #python array module - stores only one specific data type, but first it need to import
# #numpy arrays( python module ) - binding c libraries used for data science
# #python is best for DS,ML

# # list vs string
# # strings are immutable
# # in same string it can't change its value after it is assigned, for changing u need to assigned in new string
# # s = "string"
# # s.title()
# # print(s)
# # t = s.title() # title capitals first letter of string
# # print(t)
# # list are mutable
# l = ["word1","word2","word3"]
# l.pop()
# print(l)

# #looping in list
# #for loop
# # fruits = ["Orange","Apple","Mango","Grapes","Apple"]
# # for fruit in fruits:
# #     print(fruit)

# #while loop
# fruits = ["Orange","Apple","Mango","Grapes","Apple"]
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# # list inside lists 
# matrix = [[1,2,3],[4,5,6],[7,8,9]] # 2d list ---- list inside list
# print(matrix[0])
# print(matrix[1])
# print(matrix[2])

# for sublist in matrix:
#     for i in sublist:
#         print(i)

# print(matrix[2][0])

# #type function
# s = "string"
# print(type(s))
# print(type(matrix))

# #generate lists with range function
# numbers = list(range(1,21))
# print(numbers)
# #something more about pop method
# numbers = list(range(1,21))
# popped_number = numbers.pop() # pop method also returns value it pops
# print(numbers)
# #index method
# numbers = [1,2,3,4,5,6,7,8,9,0,1,12,34,2,1]
# print(numbers.index(1))
# print(numbers.index(1,3))
# print(numbers.index(1,3,9))
# print(numbers.index(1,-1))
# #pass list to a function
# numbers = [1,2,3,4,5,6,7,8,9,10]
# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative
# print(negative_list(numbers))

# #Exercise
# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square

# numbers = list(range(1,11))
# print(square_list(numbers))

# #Exercise
# # def reverse_list(l):
# #     l.reverse()
# #     return l

# # numbers = list(range(1,5))
# # print(numbers)
# # print(reverse_list(numbers))
# # #OR usinf string slicing
# # def reverse_list(l):
# #     return l[::-1]

# # numbers = list(range(1,5))
# # print(numbers)
# # print(reverse_list(numbers))
# #OR using pop and append
# def reverse_list(l):
#     rlist = []
#     for i in range(len(l)):
#         rlist.append(l.pop())
#     return rlist

# numbers = list(range(1,5))
# print(numbers)
# print(reverse_list(numbers))

# #Exercise
# def reverse_list(l):
#     elements = []
#     for i in l:
#         elements.append(i[::-1])
#     return elements

# numbers = ['abc','tuv','xyz']
# print(numbers)
# print(reverse_list(numbers))

# #Exercise
# def odd_even(l):
#     odd = []
#     even = []
#     for i in l:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
        
#     print(odd)
#     print(even)
#     new_list = [odd, even]
#     print(new_list)
# numbers = [1,2,3,4,5,6,7,8]
# print(numbers)
# print(odd_even(numbers))

# #Exercise
# def common_list(l1,l2):
#     flist = []
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 flist.append(i)
#     return flist

# list1 = [1,2,5,8]
# list2 = [1,2,7,6]
# print(common_list(list1,list2))

# #max min functions
# numbers = [6,60,2]
# print(min(numbers))
# print(max(numbers))

# def greatest_diff(l):
#     return max(l) - min(l)

# print(greatest_diff(numbers))

# #Exercise
# def inside_list(l):
#     c = 0
#     for i in l:
#         if type(i) == list:
#             c+=1
#     return c
# numbers = [1,2,3,[2,3,4],[34,4]]
# print(numbers)
# print(inside_list(numbers))