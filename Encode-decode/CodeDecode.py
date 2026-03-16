import random 
import string
def encode_msg(a):
    newwords = []
    for word in a:
        if(len(a) >=3):
            beg = ''.join(random.choices(string.ascii_letters, k=3))
            end = ''.join(random.choices(string.ascii_letters, k=3))
            new =  beg + a[1:] + a[0] + end
            newwords.append(new)
        else:
            newwords.append( a[::-1])
        
    print(f"Your encoded string is {newwords}")


def decode_msg(a):
    newwords = []
    for word in a:
        if(len(a) >=3):
            new = a[len(a)-4] + a[3:len(a)-4]
            newwords.append(new)
        else:
            newwords.append( a[::-1])
        print(f"Your encoded string is {newwords}")


print("Lets Code and Decode a message")
strab = input("Enter a string: ")
opr = input("Press A to encode and B to decode a message : ")
words = strab.split(" ")
if opr.upper() == "A":
    newwords = []
    for word in words:
        if(len(word) >=3):
            beg = ''.join(random.choices(string.ascii_letters, k=3))
            end = ''.join(random.choices(string.ascii_letters, k=3))
            new =  beg + word[1:] + word[0] + end
            newwords.append(new)
        else:
            newwords.append( word[::-1])
        
    print(f"Your encoded string is {newwords}") 
else:
    newwords = []
    for word in words:
        if(len(word) >=3):
            new = word[len(word)-4] + word[3:len(word)-4]
            newwords.append(new)
        else:
            newwords.append( word[::-1])
    print(f"Your encoded string is {newwords}")

