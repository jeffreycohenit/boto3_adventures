#Example
my_variable = "A string"
print(type(my_variable))


# Example of type error
my_number = 50
some_string = "The number is "
print(some_string + my_number)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

# Solution
my_number = 50
some_string = "The number is "
print(some_string + str(my_number))
The number is 50