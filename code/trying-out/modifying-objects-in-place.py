a_list = [1, 2, 3]
a_dict = {'hello': 'world'}
a_tuple = (1, 2, 3)
a_string = "Hello "
a_number = 123.45

a_list = a_list + [4]

print(a_list)

a_list += [4]

print(a_list)

a_list.sort()

print(a_list)

a_list = sorted(a_list)

print(a_list)

print(a_tuple)

a_tuple = a_tuple + (4, 5)

print(a_tuple)

a_tuple += (4,5)
print(a_tuple)

a_dict['hello'] = 'WORLD'
print(a_dict)
a_dict = dict(a_dict)
print(a_dict)
