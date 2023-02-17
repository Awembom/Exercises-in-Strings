vowels = "aeiouAEIOU"
string = input("Enter the string: ")
Nstring = ''
for characters in string:
    if characters not in vowels:
        Nstring += characters
print(Nstring)

#program to take a string and display just the consonants
#this is removing vowels