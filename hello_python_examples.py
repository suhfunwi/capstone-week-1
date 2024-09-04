
print('Hello Python!')
# Variables
school = 'MCTC'
# string
gpa = 3.7
# float
students_in_class = 22
# integer
# python automatically identifies different variables on
# its own without you having to specify
# variables use lower case joined with underscores


# if-statements
if gpa == 4:
    print('Wow!')
elif 3 <= gpa < 4:
    print('Awesome!')
else:
    print('Cool!')
#     quick if statement example to refresh
# if-elif-else

# lists
schools = ['MCTC', 'DCTC', 'NDSU']
if 'MCTC' in schools:
    # in operator
    print('MCTC is one of the schools in the list')
    schools.sort()
    print(schools)
    schools.append('Century college')
#     append adds on to the end of the list

# strings
class_name = 'Software development capstone'
print(class_name.upper())
# uppercase
print(len(class_name))
# length of string
print(class_name.strip())
if 'capstone' in class_name:
    print('This must be the capstone')
# strip removes whitespace at beginning and end

# loops - for loops over range
for x in range(10):
    print(x)
#     counting loop that goes up to the range of 10, not including 10


# loops - for loops over sequence
for s in schools:
    print(s.upper())
for letter in school:
    print(letter)
#     prints every letter in sequence
for letter in school:
    print(letter * 10)

data = [0] * 10
print(data)
# makes a new list with 10 zeros in it

# while loops
# name = input('Enter your name: ')
# # while len(name) == 0:
# # this is a shorter version
# while not name:
#     print('Please enter something')
#     name = input('Enter your name: ')

# True and False and None
start_of_semester = True
winter = False

if winter:
    # blank is a boolean, t or f
    print('brr!')
else:
    print('It is not winter')
#  Dictionaries
class_codes = {2905: 'Capstone', 2560: 'Web', 2545: 'Java'}
# key value pairs must be unique so they can be identified
print(class_codes[2560])

for code in class_codes:
    print(code)
    print(class_codes[code])
#     prints both the key and value over a loop

for code, name in class_codes.items():
    print(f'The class code is {code}   and the name is {name}')

    # print('The class code is ' +str(code) + ' and the name is ' + name)
#     python doesn't allow concatenating strings to integers
#     to make it a bit tidier use format strings(f)
#     and place it at the start of the string then
#     use curly braces for the variables

# Slicing strings, lists
schools = ['MCTC', 'DCTC', 'NDSU']
# first_two = schools[0:2]
first_two = schools[:2]
# small shortcut is omitting the first number so it automatically starts at the beginning
print(first_two)
# slices the list, so it only prints up to the 2nd index,
# meaning it prints index 0 and 1
last_school = schools[-1]
print(last_school)
# negative numbers are a small shortcut to get the last position in a list
last_two_schools = schools[-2:]
# to get multiple, specify where to start and if the end is empty,
# will automatically go to the end of the list
print(last_two_schools)
school_name = 'Minneapolis Community and Technical College'
city = school_name[:11]
print(city)
# slicing strings works the same way for lists,
# just that the indexes are for individual letters

# File IO(input/output)
with open('data.txt') as f:
    print(f.read())
#     code won't work because we don't have a file named data.txt,
#     but what would happen is that it reads it and prints it out
# update: added a data.txt filem and it does work now
with open('schools.txt', 'w') as f:
        f.writelines(schools)
#     this writes the schools list into the schools.txt file

# Functions


def get_name():
    # define the function with def
    print('Hello, please enter your name!')
    username = input('Your name is: ')
    return username
# don't forget to return the value of the function at the end


name = get_name()
