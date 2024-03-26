user_string = input("Enter a string: ")

print("This is what I found about the string:")

if user_string.isalnum():
    print('The string is alphanumeric.')
if user_string.isdigit():
    print('The string contains only digits.')
if user_string.isalpha():
    print('The string contains only alphabet letters.')
if user_string.isspace():
    print('The string contains whitespace characters.')
if user_string.islower():
    print('The letters in the string are all lower case.')
if user_string.isupper():
    print('The letters in the string are all upper case.')