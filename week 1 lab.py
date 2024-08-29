name = input('What is your name?')
birthmonth = input('What is your birth month?')
name_length = len(name)

if birthmonth == 'August':
    print('Hello ' + name + '!')
    print('Your name has ' + str(name_length) + ' letters in it')
    print('Happy birthday ' + name + '!')
else:
    print('Hello ' + name + '!')
    print('Your name has ' + str(name_length) + ' letters in it')

class_names = []
classes = input('What classes are you taking?')
class_names.append(classes)

for c in class_names:
    print(class_names)