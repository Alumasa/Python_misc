# this code receives an input and prints out the divisors of that input in a range of 2 to 100.
num = int(input("Provide a number: "))
div_list = []
x = range(2, 101)
for each in x:
    if num % each == 0:
        div_list.append(each)
print(div_list)