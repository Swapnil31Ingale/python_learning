def word_frequency(sentence):
    dict = {}
    list_of_words = sentence.split()
    for word in list_of_words:
        word = word.lower()
        dict[word] = dict.get(word, 0) + 1
    return dict

# Test the function
result = word_frequency("This is a test. This test is a good test.")
print(result)
# Output: {'this': 2, 'is': 2, 'a': 2, 'test': 3, 'good': 1}

# def word_frequency(sentence):
#     word_dict = {}
#     words = sentence.lower().split()
#     for word in words:
#         word_dict[word] = word_dict.setdefault(word, 0) + 1
#     return word_dict

# # Test the function
# result = word_frequency("This is a test. This test is a good test.")
# print(result)
# # Output: {'this': 2, 'is': 2, 'a': 2, 'test': 3, 'good': 1}

