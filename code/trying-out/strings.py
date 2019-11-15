word = 'tomek'

for i in range(-1,-len(word)-1,-1):
    print(word[i])


print(word[1:4])
print(word[-4:-1])
print(word[::-1])
print(word[0:len(word):2])
print(word[1:len(word):2])

print('format-=====')
print(word+ '{}'.format('kappa'))


