# f-strings

# Concatenating strings and numbers

name = "Jane"
age = 28


# Avoiding conversions like str(number):
# print(name + " is " + str(age) + " years old")
# >Bob is 33 years old


# Use the .format() method:

print("{name} is {age} years old".format(name=name, age=age))
# >Jane is 28 years old


# Use f-strings:

print(f"{name} is about {age * 364} days old")
# >Jane is about 10192 days old

input()