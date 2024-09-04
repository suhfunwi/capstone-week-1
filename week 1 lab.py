name = input('What is your name?')
birth_month = input('What is your birth month?')
name_length = len(name)
print(f'Hello, {name}!')
print(f'There are {len(name)} letters in your name')
# can put simple expressions in format strings
# They are your friend
if birth_month.lower() == 'august':
    print('Happy birthday month!')

# if birth_month == 'August':
#     print('Hello ' + name + '!')
#     print('Your name has ' + str(name_length) + ' letters in it')
#     print('Happy birthday ' + name + '!')
# else:
#     print('Hello ' + name + '!')
#     print('Your name has ' + str(name_length) + ' letters in it')
# this is my first solution, the example code made more
# sense and was much cleaner, so I'll go with that


classes = []
class_name = input('Enter class name? Press enter to quit. ')
while class_name:
    classes.append(class_name)
    # adds the classes in the list
    class_name = input('Enter class name. Press enter to quit. ')
    print(classes)
    for c in classes:
        print(c)
#         for loop makes it print line by line
#     for index, c in enumerate(classes):
#         print(index, c)
# doing this method will also make the index number
# print in front of the class name



# class_names = []
# classes = input('What classes are you taking?')
# class_names.append(classes)
#
# for c in class_names:
#     print(class_names)
# My original code. Put all the classes in a list instead of printing one by one.
# looks like all I was really missing was a for loop
