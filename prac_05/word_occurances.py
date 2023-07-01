"""
Word Occurrences
Estimate: 60 minutes
Actual:   70 minutes
"""

text = input("Please input text: ")
string_split = text.split(" ")
dictionary = {}
max_length = 0
for word in string_split:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
    if len(word) > max_length:
        max_length = len(word)
sorted_dict = dict(sorted(dictionary.items()))
print(sorted_dict)

for key in sorted_dict:
    print(f"{key:{max_length}}: {sorted_dict[key]}")
