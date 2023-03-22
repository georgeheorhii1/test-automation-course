import re


# Task_1
def check_valid_string(s):
    pattern = r'^[a-zA-Z0-9_]+$'
    return bool(re.match(pattern, s))


string1 = "hello_world_123"
string2 = "This is invalid."
print(check_valid_string(string1))
print(check_valid_string(string2))


# Task_2
def remove_brackets(text):
    pattern = r'\(.*?\)'
    return re.sub(pattern, '', text)


text = '["example (.com)", "github (.com)", "stackoverflow (.com)"]'
output = remove_brackets(text)
print(output)


# Task_3
def insert_space(text):
    pattern = r'(?<=\w)([A-Z])'
    return re.sub(pattern, r' \1', text)


# Example usage:
text = "InsertSpaceBeforeUppercaseLetters"
output = insert_space(text)
print(output)
