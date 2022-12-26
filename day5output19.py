def extract_consonant(s):
    consonant=0
    for i in s:
        if i in 'BCDEFGHIJKLMNOPQRSTUVWXYZ':
           consonant+=1
    return consonant
str1=input()
a=extract_consonant(str1)
print("consonants in:",str1," ' is",a)
