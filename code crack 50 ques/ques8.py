# Write a Python program to classify a character as vowel or consonant.
x=input(" enter a character  ").lower()
if(len(x)==1 and x.isalpha()):
    if(x==("a" or "e" or"i" or"u" or"o") ):
        print("the given character is a vowel")
    else:
        print("the given character is a consonant")
else:
    print("invalid input please enter a valid  single  character ")