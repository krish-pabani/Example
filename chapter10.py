# dictionary comprehension
# # square = {1:1, 2:4, 3:9} # key:value
# square = {num:num**2 for num in range(1,11)}
# print(square)

# # OP ----> square of 1 : 1
# # OP ----> square of 2 : 4
# square = {f"Square of {num} is":num**2 for num in range(1,11)}
# print(square)

# for k,v in square.items():
#     print(f"{k} : {v}")

# string = 'Jhonesh'
# word_count = {char:string.count(char) for char in string}
# print(word_count)

# # dictionary comprehension with if else
# # d = {1:'odd', 2:'even' ... }
# odd_even = {i:('even' if i%2 == 0 else 'odd') for i in range(1,11)}
# print(odd_even)

# # sets comprehension
# s = {k**2 for k in range(1,11)}
# print(s)

# names = ['harshit','mohit','rohit']
# first = {charfirst[0] for charfirst in names}
# print(first) # since it is set so OP will be unordered