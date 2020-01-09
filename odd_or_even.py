#checks if the input is odd or even
number = int(input('Please input a number:'))

if number % 2 == 0:
    print(str(number) + " is even.")
    if number % 4 == 0:
        print(str(number) + " is even, and a multiple of 4.")
else:
    print(str(number) + " is odd.")


check = int(input("Put a number: "))
num = int(input("Put a second number: "))

if check % num == 0:
    print(str(check) + " divides evenly into " + str(num) + ".")
else:
    print(str(check) + " does NOT divide evenly into " + str(num) + ".")


