#URL ENCODE RAW TEXT TO %XX ESCAPE CHARACTER
import urllib.parse
raw_text = input("Enter Text to Encode : ")
encoded_text = urllib.parse.quote(raw_text, safe='/', encoding=None, errors=None)
print("RAW TEXT : {} \nENCODED TEXT : {}".format(raw_text, encoded_text))
