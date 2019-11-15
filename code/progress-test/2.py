def firstRepeatedWord(s):
    chars = ',.:;-'
    test_list = []
    test_dir = {}
    
    for c in chars:
        s = s.replace(c, '')
    test_list = s.split(' ')

    for word in test_list:
        if word in test_dir:
            test_dir[word] += 1
            if test_dir[word] == 2:
                return word
        else:
            test_dir[word] = 1
    




test_string = 'He had had quite: enough, of. this- nonsense.'



test_dir = {}



print(firstRepeatedWord(test_string))
    