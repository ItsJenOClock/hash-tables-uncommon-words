def uncommon_from_sentences(s1, s2):
    uncommon_words = []
    word_dict = {}

    for word in s1.split():
        word_dict[word] = word_dict.get(word, 0) + 1
    for word in s2.split():
        word_dict[word] = word_dict.get(word, 0) + 1
    
    for word, count in word_dict.items():
        if count == 1:
            uncommon_words.append(word)
    
    return uncommon_words
