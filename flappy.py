# Legendary hello world
print('Hello World')

# basic arithmetic
print(1+1)

print(2 * 3)

print(1/2)

print(2**4)

print(4 % 2)

print(5 % 2)

print((2+3) * (5-2))

# Variables
name = 'Mubin'
print(name)

# Variable names cannot start with number or special characters
x = 4
y = 9

z = x + y
print(z)

# Strings
print('in single quotes')
print("in double quotes")
print("Mubin's cat is Ginger")

# F strings
favourite_number = 6
print('My name is ' + name + ' and my favourite number is ' + str(favourite_number))
print(f'My name is {name} and my favourite number is {favourite_number}')

# Lists
my_list = [1,2,3]
print(my_list)

my_list = ['hi', 2,3, [4,5]]
print(my_list)

my_list = ['a', 'b', 'c']
my_list.append('d')
print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[1:])
print(my_list[:2])

my_list[0] = 'NEW'
print(my_list)

my_list = ['hi', 2,3, [4,5, [7,8,9]]]
print(my_list[3][2][0])

# Tuples
t = (1,2,3)
print(t[0])

# this will give an error
t[0] = 'NEW'

# Dictionaries
d = {'key1': 'item1', 'key2': 'item2'}
print(d)
print(d['key1'])

# Booleans
print(True)
print(False)

# Comparison Operator
print(1 > 2)
print(1 < 2)
print( 1 >= 1)
print(1 <= 4)
print(10 == 10)
print('hi' == 'bye')

# if, elif, else
if 1 < 2:
	print('Yep!')

x = 12
if (x % 2 == 0):
	print('Divisible by 2')
elif x % 3 == 0:
	print('Divisible by 3')
else:
	print('Not divisible by 2 or 3!')

# Conditional operators - and, or

if (x % 2 == 0 and x % 3 == 0):
	print('Divisible by 2 and 3')
elif (x % 2 == 0):
	print('Divisible by 2')
elif x % 3 == 0:
	print('Divisible by 3')
else:
	print('Not divisible by 2 or 3!')

age = 19
is_drunk = False

# if (age < 18 or is_drunk == True): this line and the below line are same
if (age < 18 or is_drunk):
	print('You cannot drive!')
else:
	print('You can drive!')

# For loop
my_list  = [1,2,3,4,5]
print(my_list[0])
print(my_list[1])
print(my_list[2])

for item in my_list:
	print(item)

for item in my_list:
	print('yep')

for jelly in my_list:
	print(jelly + jelly)


# While loop
i = 1
while (i < 5):
	print(f'i is {i}')
	i = i + 1

i = 1
while(True):
	print(f'i is {i}')
	i = i + 1
	if (i == 5):
		break

# Range
for i in range(0, 5):
	print(i)

# Functions

# I cannot reuse this!
num = 2
if (num % 2 == 0):
	print(f'{num} is even!')
else:
	print(f'{num} is odd!')

def check_even_odd(num):
	if (num % 2 == 0):
		print(f'{num} is even!')
	else:
		print(f'{num} is odd!')

check_even_odd(2)
check_even_odd(3)
check_even_odd(5)
print(check_even_odd(8))

def calculate_square(num):
	# return num * num
	return num ** 2

calculate_square(2)
print(calculate_square(2))