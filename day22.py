# Remove all whitespaces from string

import re

text = "    Sirisha  KVL "
print("Removing all whitespaces from string:",re.sub(r'\s+','',text))