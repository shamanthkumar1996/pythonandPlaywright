text = "apple banana apple orange banana apple"

def fin_most_repeated(s):
    words = s.split(" ")
    freq = {}
    max_word = ""
    max_count = 0
    for word in words:
       freq[word] = freq.get(word,0) +1

       if freq[word] > max_count:
           max_count = freq[word]
           max_word = word

    return max_word
print(fin_most_repeated(text))