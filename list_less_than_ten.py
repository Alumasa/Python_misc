#this code prints out a new list which contains numbers in the list, less than the input
a = [1, 5, 7, 8, 45, 89, 0, 3, 23,10.0 ]
new_a = []
num = int(input("Give a number: "))
for number in a:
    if number < num:
        new_a.append(number)
print(new_a)
