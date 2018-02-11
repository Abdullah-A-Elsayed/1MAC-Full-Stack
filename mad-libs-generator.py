# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if(word=="NOUN"):return random_noun()
    elif (word=="VERB"):return random_verb()
    elif (word!=''): return word[0]
    return ''
# print word_transformer("hello")
# print word_transformer("NOUN")
# print word_transformer("VERB")
# print word_transformer("")

#Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is

def process_madlib(mad_lib):
    processed = ""
    i=0
    while(i<len(mad_lib)):
        word = mad_lib[i:i+4]
        replacement = word_transformer(word)
        processed+=replacement
        i+=1
        if (len(replacement) > 1):
            i+=3
    return processed
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)