def is_palindrome(s):
    s = s.lower()
    modified_string = ''
    for char in s:
        if char.isalnum():
            modified_string  += ''.join(char)
            #modified_string += char
            #print(modified_string)
    reverse_string = modified_string[::-1]
    #print(reverse_string)
    if modified_string == reverse_string:
        return True
    else:
        return False

# Test the function
print(is_palindrome("radar"))  # Should return True
print(is_palindrome("hello"))  # Should return False
print(is_palindrome("A man a plan a canal Panama"))  # Should return True
print(is_palindrome("This is False case"))

# import re
# def remove_spaces_and_punctuation(s):
#     return re.sub(r'[^a-zA-Z0-9]', '', s)

# def is_palindrome(s):
#     s = s.lower()
#     s = ''.join(char for char in s if char.isalnum())
#     return s == s[::-1]

# # Test the function
# print(is_palindrome("radar"))  # Should return True
# print(is_palindrome("hello"))  # Should return False
# print(is_palindrome("A man a plan a canal Panama"))  # Should return True
