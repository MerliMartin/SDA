"""
Write a function that will return the 5 most common words from
Mickiewicz's work. https://pastebin.com/raw/aAHeW5Pt (copy and save
to a text file what you will find at this link).
Hint: use the open() function, split() method, dictionary and loop
"""


def find_most_used_words_from_text(text_file):
    with open(text_file, encoding="utf8") as f:
        text_from_file = f.read().lower().split()
        dict_for_words_count = {}
        for word in text_from_file:
            if word in dict_for_words_count:
                dict_for_words_count[word] += 1
            else:
                dict_for_words_count[word] = 1
        sorted_words = sorted(((value, key) for (key, value) in dict_for_words_count.items()), reverse=True)[:5]
        print(sorted_words)  # [(12, 'w'), (7, 'i'), (6, 'się'), (6, 'do'), (6, 'a')]


find_most_used_words_from_text("Mickiewicz.txt")
