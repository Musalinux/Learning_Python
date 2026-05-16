import re

text = "Today is a sunny day"
pattern = r"sunny"

match = re.search(pattern, text)

if match:
    print ("found the text:", match.group())
else:
    print ("No match")