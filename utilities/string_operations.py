
string = "Alpha"

def reverse_string(string):
    reduced = string[::-1]
    return reduced



def capitalize_string(string):
    upper = string.title()
    return upper



def lowercase_string(string):
    lower = string.lower()
    return lower



def uppercase_string(string):
    upper = string.upper()
    return upper


print(reverse_string(string))
print(capitalize_string(string))
print(lowercase_string(string))
print(uppercase_string(string))