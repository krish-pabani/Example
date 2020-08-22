# #set data type
# # unordered collections of unique items

# s = {1,2,3,2} 
# print(s) # OP will remove duplicate values ----> {1,2,3}
# # #print(s[1]) # Index value print will not work in set
# # l = [1,2,3,4,5,5,5,5,6,6,7,8,8,6]
# # s2 = set(l) # remove duplicate, list is converted to set
# # s2 = list(set(l)) # change it again to list
# # print(s2)
# # #add in set
# # s.add(4)
# # s.add(5)
# # print(s)
# # #remove in set
# # s.remove(3)
# # # s.remove(6) # error coz 6 is not present in set
# # print(s)
# # #discard method
# # s.discard(2)
# # s.discard(6) # since 6 is not present in set but discard method doesn't show it as error
# # print(s)
# # clear method 
# # s.clear()
# # print(s) # will clear whole set
# # copy method
# s1 = s.copy()
# print(s1)

# # in set we can't store list & dictionary

# # in keyword in set 
# s = {'a','b','c'}

# if 'a' in s:
#     print("Present")
# else:
#     print("Not Present")

# # loop in set
# for item in s:
#     print(item) # can get unordered output

# # to remove duplicate values set is best for it

# # union ----> |
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print(s1 | s2) 

# #intersection ----> &
# print(s1 & s2)

