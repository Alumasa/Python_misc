name = input("Please enter your name: ")
input_age = input("Please enter your age: ")

age = int(input_age)

year_of_birth = 2020 - age
year_of_hundred = year_of_birth + 100

print(name, "you will turn 100 years old in the year", year_of_hundred)

#a code snippet on granting access
#passwordFile = open('SecretPasswordFile.txt')  #commented out because there is no .txt file.
secretPassword = passwordFile.read()
typedPassword = input('Enter your password:')
if typedPassword == secretPassword:
    print('Access Granted!')
elif typedPassword == '12345':
    print('What do you take me for??')
else:
    print('Access Denied!!')

#this one finds patterns of numbers within a text
import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4242')
print('Phone number found:' + mo.group())

# Use of sorted()
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse=True)

# Print out full_sorted
print(full_sorted)
