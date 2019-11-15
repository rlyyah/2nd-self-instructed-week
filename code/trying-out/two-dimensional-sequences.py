# list of lists

my_table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

print(my_table)
for i in range(len(my_table)):
    for j in range(len(my_table[i])):
        print(my_table[i][j])

# 3d list (list of list of lists)
print('=============================')
print('3d list (list of list of lists)')

my_3d_list = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]
print(my_3d_list[0][0][0])

# defying long lists

my_long_list = [0] * 100 # a long list of zeros
print(my_long_list)

day = [""] * 24
print(day)

timetable = [day] * 7
print(timetable)

timetable[1][12] = 'meeting with Julia'
print(timetable)


timetable = [[""] * 24 for day in range(7)]
timetable[1][12] = 'meeting with Julia'
print(timetable)
print('==============')

a = [
    (1,),
    (2, 2),
    (3, 3, 3),
]
print(a)
print(a[1][1])

b = [[''] * 4 for i in range(4)]
b = [
    list(range(10)),
    list(range(10, 20)),
    list(range(20, 30)),
    list(range(30, 40)),
]
print(b)

print(b[0][1:-1])

