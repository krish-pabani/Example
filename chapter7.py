    # Dictionaries
# why dictionaries
# Because of limitations of lists, lists are not enought to represent real data 
# what are dictionaries 
# unordered collections data in key : value pair

# #how to create dictionaries 
# user = {'name' : 'Jhonesh', 'age' : 24}
# print(user)
# print(type(user))
# # OR
# user1 = dict(name = 'Jhonesh', age = 24)
# print(user1)
# print(type(user1))
# #  dicitionary don't have indexs, it has key 
# print(user['name'])
# print(user['age'])

# # dictionary can have strings lists numbers dictionary

# user_info = {
#     'name' : 'Jhonesh',
#     'age' : 24,
#     'fav_movies' : ['coco','kimi'],
#     'fav_tunes' : ['awaken', 'tale']
# }
# print(user_info['fav_movies'])

# # how to add data in empty dictionary 
# user_info2 = {}
# user_info2['name'] = 'Mohit'
# user_info2['age'] = 20
# print(user_info2)

# user_info = {
#     'name' : 'Jhonesh',
#     'age' : 24,
#     'fav_movies' : ['coco','kimi'],
#     'fav_tunes' : ['awaken', 'tale']
# }
# # to check if key exists in dicitonary 
# if 'name' in user_info:
#     print('Present')
# else:
#     print('Not present')
# # oto check it value exists in dictionary 
# if 'Jhonesh' in user_info.values():
#     print('Present')
# else:
#     print('Not present')

# # loops in dictionaries
# # to print all keys 
# for i in user_info:
#     print(i)
# # to print all values
# for i in user_info.values():
#     print(i)

# # values method 
# user_info_values = user_info.values()
# print(user_info_values) # will print as list but it's type is dict_values
# print(type(user_info_values))

# # keys method 
# user_info_keys = user_info.keys()
# print(user_info_keys) # will print as list but it's type is dict_keys
# print(type(user_info_keys))

# # to print values wirth help of keys
# for i in user_info:
#     print(user_info[i])

# # items method ----IMPORTANT
# user_info = {
#     'name' : 'Jhonesh',
#     'age' : 24,
#     'fav_movies' : ['coco','kimi'],
#     'fav_tunes' : ['awaken', 'tale']
# }
# # user_item = user_info.items()
# # print(user_item)
# # print(type(user_item))
# # OP it is not list----> [('name', 'Jhonesh'), ('age', 24), ('fav_movies', ['coco', 'kimi']), ('fav_tunes', ['awaken', 'tale'])]
# for key, value in user_info.items():
#     print(f"key is {key} and value is {value}")

# # add and delete data
# user_info = {
#     'name' : 'Jhonesh',
#     'age' : 24,
#     'fav_movies' : ['coco','kimi'],
#     'fav_tunes' : ['awaken', 'tale']
# }

# # # how to add data
# # user_info['fav_songs'] = ['song1','song2']
# # print(user_info)

# # # how to delete data --- pop method
# popped_item = user_info.pop('fav_tunes') # here pop method needs atleast one argument
# print(f"popped item is {popped_item}")
# print(user_info)
# print(type(popped_item))

# # popitem method --- randomly deletes any key 
# popped_item = user_info.popitem()
# print(popped_item)
# print(user_info)
# print(type(popped_item))

# # update dictionary 
# user_info = {
#     'name' : 'Jhonesh',
#     'age' : 24,
#     'fav_movies' : ['coco','kimi'],
#     'fav_tunes' : ['awaken', 'tale']
# }

# more_info = {'State' : 'Gujarat', 'hobbies' : ['coding', 'reading','guitar']} # if in this dictionary there is any same key that above dictionary has then after updating dictionary previous value will be replaced by new value of a particular common key
# user_info.update(more_info)
# print(user_info)

# # fromkeys method
# # if different keys have same values
# # d = {'name' : 'unknown', 'age' : 'unknown', 'height' : 'unknown'}
# d = dict.fromkeys(['name', 'age', 'height'], 'unknown') # as list
# print(d)
# d = dict.fromkeys(('name', 'age', 'height'), 'unknown') # as tuple
# print(d)
# d = dict.fromkeys('abc', 'unknown') # if one single argument then it will treat string's all character as different keys in this a b c
# print(d)
# d = dict.fromkeys(range(1,11), 'unknown')
# print(d)
# d = dict.fromkeys(['name', 'age'], ['unknown','unknown'])
# print(d)

# # get method 
# d = {'name' : 'Jhon', 'age' : 'unknown', 'height' : 'unknown'}
# print(d['name'])
# # print(d['names']) # error
# print(d.get('name'))
# print(d.get('names')) # will return NONE as there is no such key name names

# if 'name' in d:
#     print('present')
# else:
#     print('not present')
# # OR 
# if d.get('name'):
#     print('present')
# else:
#     print('not present')

# # copy method 
# d = {'name' : 'Jhon', 'age' : 'unknown', 'height' : 'unknown'}
# d1 = d.copy()
# print(d)
# print(d1)
# print(d1 is d) # it will saw false coz dictionary is different but as copied data
# print(d.popitem())
# print(d)
# print(d1)

# d2 = d
# print(d2 is d) # it will return true coz it is not a copy, it is same dictionary

# # clear method 
# d = {'name' : 'Jhon', 'age' : 'unknown', 'height' : 'unknown'}
# print(d)
# d.clear()
# print(d)

# # more about get, two same keys in dicitionaries
# user = {'name' : 'Jhon', 'age' : 24, 'age' : 34}
# print(user.get('name'))
# print(user.get('names')) # be default if dicitionary has not that particular key then it returns None
# print(user.get('fav', 'Not Found!')) # if that key is not present then it will return Not Found!
# print(user) # if there is same particular keys then latest values will be counted which overrides old value

# #Exercise
# def cube_finder(n):
#     dict_cube = {}
#     for i in range(1,n+1):
#         dict_cube[i] = i**3
#     return dict_cube

# number = int(input("Enter number till that you want cubes: "))
# print(cube_finder(number))

# # Word counter Program
# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count

# print(word_counter("harshit"))

# #Exercise

# users = {}
# users['name'] = input("Enter your name :")
# users['age'] = input("Enter your age :")
# users['fav_movie'] = list(input("Enter your favorite movies :").split(","))
# users['fave_songs'] = list(input("Enter your favorite songs :").split(","))
# print(users)

# for key, value in users.items():
#     print(f"{key} : {value}")



