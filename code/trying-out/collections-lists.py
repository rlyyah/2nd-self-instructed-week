animals = ['cat', 'dog', 'fish', 'bison']

print(animals[1:-1]) # ['dog', 'fish']
print(animals[:])
print(animals[::3])
del animals[1]
print(animals)

animals = ['cat', 'dog', 'goldfish', 'canary']
pets = animals # now both variables refer to the same list object

animals.append('aardvark')
print(pets) # pets is still the same list as animals

animals = ['rat', 'gerbil', 'hamster'] # now we assign a new list value to animals
print(pets) # pets still refers to the old list

pets = animals[:] # assign a *copy* of animals to pets
animals.append('aardvark')
print(pets) # pets remains unchanged, because it refers to a copy, not the original list

nums = [1,0,1,0]

print(len(nums))
print(sum(nums))
print(any(nums))
print(all(nums))
print(nums.count(1))
nums.extend([1,2,3,4,5])
print(nums)
nums.insert(5, 500)
print(nums)
print(list(reversed(nums)))

a = [1,3,5]
b = [0,2,4]
c = a + b 
d = list(c)
d.sort()
d = list(reversed(d))
c[3] = 42
d.append(10)
c.extend([7,8,9])
print('d' + str(d))
print(f'c {c}')
print(c[:3])
print(d[-1])
print(len(d))
