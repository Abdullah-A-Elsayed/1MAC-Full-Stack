# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    # your code here
    for speech in parts_of_speech:
    	if(speech in word):
    	 	return speech
    return None

def play_game(ml_string, parts_of_speech):    
    replaced = []
    ml_list = ml_string.split()
    for word in ml_list:
        returnee = word_in_pos(word, parts_of_speech)
    	if returnee != None:
    		user_input = raw_input("write a "+returnee+": ")
    		word = word.replace(returnee,user_input)
    	replaced.append(word)
    return " ".join(replaced)
    
print play_game(test_string, parts_of_speech)       
