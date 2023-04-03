# Split a string with multiple delimeters

import re

text = "The quick brown* fox jumps \n over the lazy dog"
print(re.split(';|,|\*|\n',text))