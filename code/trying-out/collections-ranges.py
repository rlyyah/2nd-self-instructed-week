# range is another kind of immutable sequence type. It is very specialised – 
# we use it to create ranges of integers. Ranges are also generators. 
# We will find out more about generators in the next chapter, but for now we just need to know that 
# the numbers in the range are generated one at a time as they are needed, and not all at once.
# In the examples below, we convert each range to a list so that all the numbers are generated
#  and we can print them out:

print(list(range(10)))
print(list(range(1, 11, 2)))

a = list(range(0,20,1))
print(a)
b = list(range(3,13,1))
print(b)
c = list(range(2,51,3))
print(c)