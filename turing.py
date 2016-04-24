import random
import string

def decode(word):
    message = ""
    for letter in word:
        if letter.isdigit() == True:
            skip = int(letter)
        else:
            if skip == 0:
                message = message + letter
            else:
                skip = skip - 1
    return message

print decode("0c1go9krgxsjmdtl0o5rtlwzm8yrtjgsuib5wxhgfi2tia")

def encode(word):
    message = ""
    for letter in word:
        num = random.randint(0,9)
        letters = "".join(random.sample(string.ascii_lowercase, num))
        message = message + str(num) + letters + letter
    return message

print decode(encode("colombia"))