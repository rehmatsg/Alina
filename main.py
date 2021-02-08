import backend

mode = "chat"
name = "Rehmat"

while True:
	q = input("You -> ")

	setAlina = backend.Alina(q, name, mode)

	alina = setAlina[0]
	mode = setAlina[1]
	long_text = setAlina[2]
	url = setAlina[3]

	print(alina + "\n" + long_text + "\n" + url)