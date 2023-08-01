# #Input Sentence and store as def
# print("Enter Your Sentence for Encoding")
# store all the alphabet into a list
import random
alph = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alph)


def userinput():
    x = input("Enter Your Sentence for Encoding")
    sentence = x.lower()
    return sentence


User = userinput()
# split the sentence into alphabets and store into a list


def listed_sentence():
    listed = list(User)
    return listed


User_listed = listed_sentence()


# creating a random number


def encryption():
    empty = []
    # generates a random number
    n = random.randint(0, 99)
    print("The Encryption Key is " + str(n))
    for i in User_listed:
        if i.isalpha():
            new_num = alpha_list.index(i) + n
            while new_num > 25:
                new_num = new_num - 26
            empty.append(alpha_list[new_num])
        else:
            empty.append(i)
    return empty


encrypted_alphabet = encryption()
# joining the letters to for word


def listtostring():
    new_sentence = ""
    new = new_sentence.join(encrypted_alphabet)
    return new


print(listtostring())