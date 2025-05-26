import random



chapter1 = ["Neo", "Cyber", "Xo", "New", "Git", "Xev", "Torc", "Tor", "Dir", "XZ", "Kol"]
chapter2 = ["Fun", "War", "Nat", "IO", "Vi", "Go", "Vos", "Sep", "Ti", "Tui"]

def start():
	print("Name Generator,Please, Press English 'y' to generate")
	InpUser = input()

	if InpUser == "y":
		startgen()
	else:
		start()
	


	
def startgen():
	randim = random.randint(0, 10)
	randim2 = random.randint(0, 9)
	print(chapter1[randim]+chapter2[randim2])
	start()
	

start()
