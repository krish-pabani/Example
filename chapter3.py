#if 
age = input("Enter your age: ")
age = int(age)
if age >= 14:
    print("Line a")
    print("you are above 14")

#Pass statement
x = 18
if x>18:
    pass # if we don't want to write any anything inside if statement

#if else
x = int(input("Enter your age: "))
if x >= 18:
    print("You are an adult")
else:
    print("Your under 18")

#Exercise
#Nested if else 
winning_number = 25
user_in = input("Guess number between 1 & 100: ")
user_in = int(user_in)
if user_in == winning_number:
    print("YOU WIN!")
else:
    if user_in < winning_number:
        print("TOO LOW!")
    else:
        print("TOO HIGH")

And Or Operator
and , or

#Exercise
name,age=input("Enter your name and age: ").split()
print(name)
print(age)
age = int(age)
if name.lower()[0] == "a" and age > 10:
    print("You can watch coco movie")
else:
    print("Sorry, you cannot watch coco")

#if elif else statement
# used when we have multiple conditions
age = int(input("Enter your age: "))

if age==0 or age<0:
    print("You acnnot watch")
elif 0<age<=3:
    print("Ticket Price: Free")
elif 3<age<=10:
    print("Ticket Price: 150")
elif 10<age<=60:
    print("Ticket Price: 250")
else: 
    print("Ticket Price: 200")

#in keyword
name = "Johnesh"
if 'a' in name:
    print("a is present in name")
else:
    print("Not present")

#check empty or not
name = input("Your name: ")
if name: #true if string is not empty
    print("Not Empty")
else:
    print("Empty")

#while loop
i = 1;
while i<=10:
    print(f"Hello World {i}")
    i = i + 1

total = 0
j = 1
while j <= 10:
    total += j
    j += 1
print(f"Total: {total}")

#Exercise1
total = 0
num = int(input("Enter natural number: "))
i=1;
while i<=num:
    total += i
    i += 1
print(f"Total: {total}")

#Exercise2
num = input("Enter number containing more than one digit: ")
i = 0
number = 0
while i < len(num):
    number += int(num[i])
    i += 1
print(f"Number :{number}")

#Exercise3
name = input("Enter your name: ")
i = 0
temp = ""
while i < len(name):
    if name[i] not in temp:
        temp += name[i]     
        print(f"{name[i]}:{name.count(name[i])}")
    i += 1

# Infinite Loop
i = 0
while i <= 10:
    print("Hello") #infinite loop as we haven't increment i
to stop infinite loop ctrl+c

for loop
for i in range(10): # i=0 to i=9
    print("Hello")

for i in range(1, 11): # i=1 to i=10
    print(f"Hello: {i}")

# to print for loop values in single line
for i in range(10):
            print(i, end = " ")


#to sum from 1 to 10
total = 0
num = int(input("Enter number:"))
for i in range(1,num+1):
    total += i
print(total)

total = 0
num = input("Enter number:")
for i in range(0,len(num)):
    total += int(num[i])
print(f"Total: {total}")

name = input("Enter your name: ")
i = 0
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        temp += name[i]     
        print(f"{name[i]}:{name.count(name[i])}")

# break and continue keyword
for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)

#Exercise
winning_number = 43
guess = 1
number = int(input("Guess number b/w 1 and 100: "))
game_over = False

while not game_over:
    if number == winning_number:
       print(f"You win and guessed in {guess} times")
       game_over = True
    else:
        if number < winning_number:
            print("Too Low")
            guess += 1
            number = int(input("guess again: "))
        else:
            print("To High")
            guess += 1
            number = int(input("guess again: "))
    
#DRY Don't Repeat Yourself
#Generating random number
import random
winning_number = random.randint(1,100)
guess = 1
number = int(input("Guess number b/w 1 and 100: "))
game_over = False

while not game_over:
    if number == winning_number:
       print(f"You win and guessed in {guess} times")
       game_over = True
    else:
        if number < winning_number:
            print("Too Low")
        else:
            print("To High")

        guess += 1
        number = int(input("guess again: "))

#step argument in range function
for i in range(1,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)
for i in range(0,-11,-1):
    print(i)          

# for loop in strings only for python
name = "Jhonesh"
# for any language
# for i in range(len(name)):
#     print(i)
#best for python
for i in name:
     print(i)
# adding digits of number
num = input("Enter a number: ")
total = 0
for i in num:
    total += int(i)
print(total)