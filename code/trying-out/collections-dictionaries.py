# The Python dictionary type is called dict. We can use a dictionary to store key-value pairs. 
# To define a dictionary literal, we put a comma-separated list of key-value pairs between 
# curly brackets. We use a colon to separate each key from its value. 
# We access values in the dictionary in much the same way as list or tuple elements, 
# but we use keys instead of indices:

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

personal_details = {
    "name": "Jane Doe",
    "age": 38, # trailing comma is legal
}

print(marbles["green"])
print(personal_details["name"])

print(marbles.keys())
print(marbles.values())
print(marbles.items())
print("purple" in marbles)
print("white" not in marbles)

tel_book = {'Jane Doe': '+275555367', 
            'John Smith': '+275556254',
            'Bob Stone': '+275555689'}



tel_book['Jane Doe'] = '+275551024'

print(tel_book['Jane Doe'])
tel_book['Anna Cooper']  = '+275553237'
print(tel_book)
Bob = tel_book.get('Bob')
print(Bob)
for name in tel_book:
    print(name)
    print(tel_book[name])


animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']

animals_set = set(animals)
animals_unique_list = list(animals_set)
animals_unique_tuple = tuple(animals_unique_list)
print(f'set: {animals_set}')
print(f'unique list: {animals_unique_list}')
print(f'unique tuple: {animals_unique_tuple}')


marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

colours = list(marbles) # the keys will be used by default
counts = tuple(marbles.values()) # but we can use a view to get the values
marbles_set = set(marbles.items()) # or the key-value pairs

print(colours)
print(counts)
print(marbles_set)
