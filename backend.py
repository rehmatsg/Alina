import random
import functions as fn
import json
import operator
from timefhuman import timefhuman
from googletrans import Translator

def Alina(q, name, mode):

	q_unedited = q

	translator = Translator()

	trans = translator.translate(q)

	q = trans.text
	lang = trans.src

	if lang != 'en':
		print("[TRANSLATED]" + q)

	q = q.replace("'", "")
	
	if mode == 'chat':
		with open('alina.json') as file:
			data = json.load(file)

			ratio_match_dict = dict()

			for intent in data['intents']:
				id = intent['id']

				if "--detailed" in q_unedited:
					print(id)
					q = q.replace("--detailed", "")

				for user in intent['user']:
					if fn.match(q, user) > 80:
						ratio_match_dict[id] = fn.match(q, user)
					else:
						pass

			if ratio_match_dict.items():

				if "--detailed" in q_unedited:
					print("Match Ratio: " + str(max(ratio_match_dict.items(), key=operator.itemgetter(1))))

				max_intent = max(ratio_match_dict.items(), key=operator.itemgetter(1))[0]

				for intent in data['intents']:
					tag1 = intent['id']

					if "--detailed" in q_unedited:
						print("Max Intent: " + str(max_intent) + "\n" + "This Intent: " + str(tag1) + "\n")

					if max_intent == tag1:
						response = intent['replies']
						new_mode = intent['mode']
						rand_no = random.randrange(0, len(response))
						alina_reply = response[rand_no].replace('@username', name)
						alina_reply = alina_reply.replace('@time', fn.time())

						if intent['type'] == "function":
							eval_func = eval(intent['function'].replace('@q', q))
							long_txt = eval_func[0]
							url = eval_func[1]
						else:
							long_txt = ""
							url = ""

						list_alina = [alina_reply, new_mode, long_txt, url]
						return list_alina
					else:
						pass

			else:
				list_alina = ['Sorry, I could not understand that.', mode, '', '']
				return list_alina

	else :
		mode_reply = fn.startMode(mode, q)
		list_alina = [mode_reply[0], mode_reply[1], '', '']
		return list_alina


## Response Array's Basic Content
##
## [Resp1, Resp2, Resp3, Resp4]
##
## Resp 1 -> Alina's Response
##
## Resp 2 -> New Mode, if set or return 'chat'
##
## Resp 3 -> Long content, if required, or return empty
##
## Resp 4 -> URL, if any or return empty