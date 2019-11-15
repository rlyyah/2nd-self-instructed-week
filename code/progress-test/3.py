def funWithAnagrams(test_list):
    copy_list = list(test_list)
    index_list = []
    anagrams_list = []
    for i in range(len(copy_list)):
        word = sorted(copy_list[i])
        print(word)
        word_s = ''.join(word)
        print(word_s)
        copy_list[i] = word_s
        print(copy_list)
        if word_s not in anagrams_list:
            anagrams_list.append(word_s)
            index_list.append(i)
    answer_list = []
    for el in index_list:
        answer_list.append(test_list[el])
    return sorted(answer_list)



funWithAnagrams()