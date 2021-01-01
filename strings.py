course = 'Python for "Beginners"'
print(course)
email_message = '''
Hi Sam,
Hope you are doing well. I know how you feel at the moment
Be patient and soon everything will be awesome once again!
Thanks,
Shafi
'''
print(email_message)

print('0th element is ', course[0])
# print on from Python
print('4 - 6 element is ', course[4:6])
clone_element = course[:]
print('Cloned element', clone_element)
# print a certain portion
print('Cloned_element[7:]', clone_element[7:])
print(clone_element[clone_element.index(' ') + 1:])
# Use negative to get from last character
print(clone_element[-1])
print(clone_element[-3])
# Formatted string
first = 'Muhammed Shafi'
last = 'Vayyattukavil'
formatted = f'{first} {last} is a python programmer'
print(formatted)
# String methods and general purpose fns - len is a gen purpose fn
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
# find a character or sub string and return it's starting index
print(course.replace('Beginners', 'Absolute Beginners'))
# Replace a string by another print(course.find('Beginners'))

# string methods will return new str. Does not modify the actual str
print(course)
# use in to return True or False after finding
print('Beginners' in course)