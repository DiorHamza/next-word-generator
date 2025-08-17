import random


def freq_next_word(word, text_array):
    word_count = []
    for i in range(len(text_array) - 1):
        if text_array[i] == word:
            word_count.append(text_array[i + 1])
    most_freq_word = random.choice(word_count)
    return most_freq_word


text = open("corpus.txt", "r")
text_array = text.read().lower().replace(".", "").replace(",", "").split(" ")
word = "organize"  # testing
count = 0

while count < 1000:
    next_word = freq_next_word(word, text_array)
    count += 1
    word = next_word
    print(next_word, end=" ")
