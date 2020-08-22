# # we use enumerate functions with for loop to track position of our item 
# # item in iterable 

# names = ['abc' , 'abcdef' , 'John']
# # 0 -- 'abc'
# # 1 -- 'abcdef'
# pos = 0
# for name in names:
#     print(f"{pos} --> {name}")
#     pos += 1

# # with enumrerate function

# for pos, name in enumerate(names):
#     print(f"{pos} --> {name}")



# def find_pos(l, target):
#     for pos, name in enumerate(l):
#         if name == target:
#             return pos
#     return -1

# print(find_pos(names,'John'))


# # map function
# numbers = [1,2,3,4]

# def square(a):
#     return a**2

# square = list(map(square, numbers))
# print(square)