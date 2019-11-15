def longestEvenWord(sentence):

    return sorted(pick_even(sentence_to_list(sentence)), key=lambda word: len(word), reverse=True)[0]


def pick_even(sentence):
    filtered = []
    for word in sentence:
        if len(word) % 2 == 0:
            filtered.append(word)
        else:
            filtered.append('00')
    return filtered


def sentence_to_list(sentence):
    word_list = []
    word_list = sentence.split(' ')
    return word_list    


output = longestEvenWord('hello world makaroni mather qwqwqwqwqwqwqw')
print(output)