import itertools

print(list(range(100)))

animals = ['cat', 'dog', 'fish']

for first_animal in animals:
    for second_animal in animals:
        print("Yesterday I bought a %s. Today I bought a %s." % (first_animal, second_animal))

for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)


for i in zip(range(5), range(5, 10), range(10, 15)):
    print(i)

MONTHS = ('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER')
DAYS = (31,28,31,30,31,30,31,31,30,31,30,31)

year = {}

for i in range(len(MONTHS)):
    year[MONTHS[i]] = DAYS[i]


print(year)

month_dict = dict(zip(MONTHS,DAYS))
print(month_dict)
numbers = [1, 5, 2, 12, 14, 7, 18]
animals = ['aardvark', 'cat', 'dog', 'opossum']

vowel_animals = []
for animal in animals:
    if animal[0] in 'aeiou':
        vowel_animals.append(animal.title())

print(vowel_animals)

doubles = [2 * number for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]
vowel_animals = [animal.title() for animal in animals if animal[0] in 'aeiou']

print(doubles)
print(even_numbers)

# a generator comprehension
doubles_generator = (2 * number for number in numbers)

# a set comprehension
doubles_set = {2 * number for number in numbers}

# a dict comprehension which uses the number as the key and the doubled number as the value
doubles_dict = {number: 2 * number for number in numbers}

print()
print('================')
print()
nums = list(range(1,11))
string_of_nums = ', '.join(str(el) for el in nums)
print(string_of_nums)

print()
print('================')
print()


person = {}

for prop in ["name", "surname", "age", "height", "weight"]:
    person[prop] = input("Please enter your %s: " % prop)

print(person)
