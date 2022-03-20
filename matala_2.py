def reverse(sentence, reverse_word):
    try:
        sent = sentence
        word_len = len(reverse_word)
        if reverse_word in sentence:
            word_len = len(reverse_word)
            word_index = sent.index(reverse_word)
            part1 = sent[:word_index]
            part2 = sent[word_len + word_index:]
            h = reverse_word[::-1]
            end = part1 + h + part2
            return end

        else:
            return "The word was not found"

    except:
        return "invalid input"


