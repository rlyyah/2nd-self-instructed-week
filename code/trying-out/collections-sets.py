# The Python set type is called set. A set is a collection of unique elements. If we add multiple 
# copies of the same element to a set, the duplicates will be eliminated, and we will be left with one
# of each element. To define a set literal, we put a comma-separated list of values inside curly 
# brackets ({ and }):

even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}

# subtraction: big numbers which are not even
print(big_numbers - even_numbers)
# union: numbers which are big or even
print(big_numbers | even_numbers)
# intersection: numbers which are big and even
print(big_numbers & even_numbers)
# numbers which are big or even but not both
print(big_numbers ^ even_numbers)

# this is an empty dictionary
a = {}

# this is how we make an empty set
b = set()

a = {1,2,3,4}
b = {1,3,5,7}

c = a | b
print(c)
d = a - b
print(d)
e = b - a
print(e)
g = a ^ b
print(g)
