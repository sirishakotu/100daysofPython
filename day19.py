# Check a string contains only a certain set of characters

import re

def is_allowed(string):
    cha = re.compile(r'[^a-zA-Z0-9]')
    string = cha.search(string)
    return not bool(string)
print(is_allowed("Abcd1234"))