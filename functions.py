from fuzzywuzzy import fuzz
import validators
import pafy
import datetime
import random
import wikipedia
import re
import webbrowser

def greet():
	return 'Welcome back'

def match(str1, str2):
	probability = fuzz.token_set_ratio(str1, str2)
	return probability

def is_int(n):
	if isinstance(n, int):
		return True
	if isinstance(n, float):
		return n.is_integer()
	return False

def validurl(url):
	return validators.url(url)

def strToURL(str):
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
	return url

def youtube(q):

	url = strToURL(q)

	video = pafy.new(url[0])
	
	best = video.getbest()
	#best.download()
	return ['Donwloading best quality Video for ' + video.title + ". This video has been viewed " + str(video.viewcount) + " times. Uploaded on " + video.author + "'s channel."]

def getword(str, occ):
	list = str.split()
	return list[occ]

def time():
	time = datetime.datetime.now()

	ret = time.strftime("%I:%M %A %d %B %Y")
	return ret

def startMode(mode, q):
	if mode == "rps":
		reply = playRCS(q)
		return [reply[0], reply[1]]
	elif mode == "guessthenumber":
		reply = playGuessTheNumber(q)
		return [reply[0], reply[1]]
	else:
		return ['Incorrect Settings. Restarting my service.', 'chat']

def playRCS(q):

	alina_turn = random.randrange(0, 3)
	mode = "rps"

	if alina_turn == 0:
		alina_rps = "rock"
	elif alina_turn == 1:
		alina_rps = "paper"
	else:
		alina_rps = "scissors"

	if q == "rock":
		if alina_rps == "rock":
			alina_reply = "My Move " + alina_rps + ". Oops, Nobody won"
		elif alina_rps == "paper":
			alina_reply = "My Move " + alina_rps + ". I won"
		else:
			alina_reply = "My Move " + alina_rps + ". You won"

	elif q == "paper":
		if alina_rps == "rock":
			alina_reply = "My Move " + alina_rps + ". You won"
		elif alina_rps == "paper":
			alina_reply = "My Move " + alina_rps + ". Oops, Nobody won"
		else:
			alina_reply = "My Move " + alina_rps + ". I won"

	elif q == "quit":
		mode = "chat"
		alina_reply = "OK. We'll play later."

	elif q == "scissors":
		if alina_rps == "rock":
			alina_reply = "My Move " + alina_rps + ". I won"
		elif alina_rps == "paper":
			alina_reply = "My Move " + alina_rps + ". You won"
		else:
			alina_reply = "My Move " + alina_rps + ". Oops, Nobody won"

	else :
		alina_reply = "That's not a valid move."

	return [alina_reply, mode]

def playGuessTheNumber(q):
	try:
		mode = "guessthenumber"
		alina_guess = random.randrange(1, 11)
		if int(q) == alina_guess:
			alina_reply = "Wow, you guessed the right number."
		elif q == 'quit':
			mode = "chat"
			alina_reply = "OK, let's get back to work."
		else :
			alina_reply = "Oops, That was wrong, let's try again. " + str(alina_guess) + " was the my number."

		list_alina = [alina_reply, mode]
		return list_alina
	except:
		if q == "quit":
			mode = "chat"
			alina_reply = "OK. We'll play later."
		else:
			return ["That was not a correct number. If you wish to quit, say 'quit'", "guessthenumber"]

def wiki(q):
	try:
		q = q.replace("who is", "")
		q = q.replace("what is", "")
		q = q.replace("what do you mean by", "")
		q = q.replace("what is the meaning of", "")
		q = q.replace("search wikipedia for", "")

		wiki_page = wikipedia.page(q)

		title = wiki_page.title
		summary = wiki_page.summary
		url = wiki_page.url

		list_alina = ['This is what I found for you related to ' + title + '. ' + summary, url]
		return list_alina

	except:
		list_alina = ['Sorry, I could not find any related articles for your query', '']
		return list_alina

def calculate(q):
	q = q.replace("calculate", "")

	q = q.replace("divide", "")
	q = q.replace("multiply", "")
	q = q.replace("add", "")
	q = q.replace("subtract", "-")

	q = q.replace("from", "+")
	q = q.replace("into", "*")
	q = q.replace("plus", "+")
	q = q.replace("subtract", "-")
	q = q.replace("by", "/")
	q = q.replace("of", "*")
	q = q.replace("%", "/100")

	return ["Result: " + str(eval(q)), '']

def google(q):
	q = q.replace("search google for", "")

	webbrowser.open("https://www.google.com/search?q=" + q)
	return ["Opened Google Search in browser", "https://www.google.com/"]


## Function Return Parameters
##
## [Rep1, Rep2]
##
## Rep1 -> Long or Short Text
##
## Rep2 -> URL to the Website
##