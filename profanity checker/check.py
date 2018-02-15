import urllib
def has_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
	#print connection
	response = connection.read()
	if response=="true": #or ("true" in response)
		return True
	return False

file_obj = open("words.txt")
words = file_obj.read()
#print words
if has_profanity(words):
	print "Alert, bad words found"
else:
	print "OK, your text is safe"