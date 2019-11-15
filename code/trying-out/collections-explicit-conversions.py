animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']

animals_set = set(animals)
animals_unique_list = list(animals_set)
animals_unique_tuple = tuple(animals_unique_list)
print(animals_set)
print(animals_unique_list)
print(animals_unique_tuple)


marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

colours = list(marbles) # the keys will be used by default
counts = list(marbles.values()) # but we can use a view to get the values
marbles_set = set(marbles.items()) # or the key-value pairs

print(colours)
print(counts)
print(marbles_set)

test = dict([('Janusz', 'Tracz'), ('Szymon', 'Golab')])
print(test)
print()
print('=================')
print()
# Another look at strings

s = "abracadabra"

print(len(s))
print(s.index("a"))

print(s[0])
print(s[3:5])

print('ab' in 'abcd') # True
print(['a','b'] in ['a','b','c','d']) # False

abc_list = list("abracadabra")
print(abc_list)

abc_word = ''.join(abc_list)
print(abc_word)


print("cat    dog fish\n".split())
print("cat|dog|fish".split("|"))
print("cat, dog, fish".split(", "))
print("cat, dog, fish, ham".split(", ", 2))

print()
print('======EXCERCISES======')
print()

given_list = [1,1,2,3,3]

a = tuple(given_list)
print(a)
b = list(a)
print(f"{b} of length: {len(b)}")
c = set(b)
print(f'{c} of length: {len(c)}')
d = list(c)
print(f'{d} of length: {len(d)}')

e = list(range(1,11))
print(e)

tel_book = {'Jane Doe': '+275555367', 
            'John Smith': '+275556254',
            'Bob Stone': '+275555689'}

t = list(tel_book.items())
print(t) 
v = list(tel_book.values())
print(v)
k = list(tel_book.keys())
print(k)

s = "antidisestablishmentarianism"
print(s)
s2 = sorted(s)
s2 = ''.join(s2)
print(s2)

word = "the quick brown fox jumped over the lazy dog"
w = word.split(' ')
print(w)