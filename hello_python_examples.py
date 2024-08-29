
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

#True and False and None
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

for code, name for class_codes.items():
    print('The class code is' +str(code))
# Slicing strings, lists

# File ID

# Functions