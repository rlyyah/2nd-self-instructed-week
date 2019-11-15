# Python has another sequence type which is called tuple. Tuples are similar to lists in many ways,
# but they are immutable. We define a tuple literal by putting a comma-separated list of values 
# inside round brackets (( and )):

# We can use tuples in much the same way as we use lists, except that we can’t modify the

# What are tuples good for? 
# We can use them to create a sequence of values that we don’t want to modify.


a = (1,2,3,4)
print(type(a))
b = (5,200,7,8)
c = a + b
print(c)

d = tuple(sorted(c))
print(d)
print(d[-3:])
print(len(d))