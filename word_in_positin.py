# Here's another chance to practice your for loop skills. Write code for the 
# function word_in_pos (meaning word in parts_of_speech), which takes in a string 
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech, 
# else return None.


def word_in_pos(word, parts_of_speech):
    # your code here
    for speech in parts_of_speech:

    	temp_list = word.split(speech) ##deleting speech from word
    	word2 = "".join(temp_list)
    	if(word2!=word):#some substring deleted
    	 	return speech
    return None


test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

print word_in_pos(test_cases[0], parts_of_speech)
print word_in_pos(test_cases[1], parts_of_speech)
print word_in_pos(test_cases[2], parts_of_speech)
print word_in_pos(test_cases[3], parts_of_speech)

"""
	learned: operator (((in))) can be used for (((strings))) instead of deleting and checking
"""