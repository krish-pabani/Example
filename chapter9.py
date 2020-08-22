# list comprehension
# with the help of list comprehension we can create of list in one line

# # create a list of squares from 1 to 10
# # using list
# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
# # using list comprehension
# square2 = [i**2 for i in range(1,11)]
# print(square2)

# # create a list of negative numbers
# # using list
# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)
# # using list comprehension
# negative2 = [-i for i in range(1,11)]
# print(negative2)


# # using list
# names = ['Johnesh','Virat','Monty']
# # OP should be----> ['J','V','M']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)
# # using list comprehension
# new_list2 = [name[0] for name in names]
# print(new_list2)

#Exercise
# def reverseIt(strin):
#     newl = []
#     for name in strin:
#         newl.append(name[::-1])
#     return newl

# l = ['abc','tuv','xyz']
# print(reverseIt(l))
# # using list comprehension
# def reverseIt(strin):
#     return [name[::-1] for name in strin]

# print(reverseIt(['abc','tuv','xyz']))


# # if statement using list comprehension 
# # using list
# numbers = list(range(1,11))
# # print(numbers)
# # even_nums = []
# # for i in numbers:
# #     if i%2 == 0:
# #         even_nums.append(i)
# # print(even_nums)
# # using list comprehension
# even_nums = [i for i in numbers if i%2 == 0]
# even_nums1 = [i for i in range(1,11) if i%2 == 0]
# print(even_nums)
# print(even_nums1)
# odd_nums = [i for i in numbers if i%2 != 0]
# odd_nums1 = [i for i in range(1,11) if i%2 != 0]
# print(odd_nums)
# print(odd_nums1)

# # Exercise
# # def int_str(strin):
# #     newl = []
# #     for i in strin:
# #         if type(i) == int or type(i) == float:
# #             newl.append(str(i))
# #     return newl

# # l = [True, False, [1,2,3], 1, 1.0, 3]
# # print(type(l))
# # print(int_str(l))
# # # using list comprehension
# def int_str(strin):
#     return [str(i) for i in strin if type(i) == int or type(i) == float]

# print(int_str([True, False, [1,2,3], 1, 1.0, 3]))

# # if else using list comprehension
# nums = [1,2,3,4,5,6,7,8,9,10]
# # OP---> new_list = [-1,4,-3,8] #odd should changed i negative and even should be multiplied by 2
# # using list
# new_list = []
# for i in nums:
#     if i%2 == 0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list) 
# # using list comprehension 
# new_list2 = [i*2 if (i%2 == 0) else -i for i in nums]
# print(new_list2)

# # nested list comprehension
# # OP ----> [[1,2,3],[1,2,3],[1,2,3]]
# nested_comp = []
# for j in range(3):
#     nested_comp.append([1,2,3])
# print(nested_comp)

# nested_comp = [[i for i in range(1,4)] for j in range(3)]
# print(nested_comp)


