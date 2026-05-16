arn = "arn:aws:iam::123456789012:user/john"

result1 = arn.split("/")[1]
print(result1)

result2 = arn.upper()
print (result2)

result3 = len (arn)
print (result3)

name = "My name is John"

replaceName = name.replace ("John", "Musa")
print (replaceName)

text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)