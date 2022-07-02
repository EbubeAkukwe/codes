#URL DECODE ENCODED %XX ESCAPE CHARACTER TO RAW TEXT
import urllib.parse

encoded_text = input("Enter Text to Decode : ")
raw_text = urllib.parse.unquote(encoded_text, encoding=None, errors=None)
print("ENCODED TEXT : {} \nRAW TEXT : {}".format(encoded_text, raw_text))
print(str(len(encoded_text))+"characters")
