import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
   w=w.lower()
   if w in data:
       return data[w]
   elif len(get_close_matches(w,data.keys()))>0:
       return "hey did you mean %s instead?"%get_close_matches(w,data.keys())[0]
   else:
     return "sorry the word doesn't exist please double check it."

word = input("enter the word:")
output=translate(word)
if(type(output)==list):
    for i in output:
        print(i)
else:
    print(translate(word))
