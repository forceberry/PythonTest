"""A mathematical code test that takes either 2 or 4 arguments.

The first argument is the name of the source file containing numbers
The second argument is the action (sum/avg/median)
The third argument is an optional comparative operation
The fourth argument is a numerical value to be used in the comparison
The results are displayed in Finnish"""
import sys
import os
messageOperation = ("Anna operaatio:\n\tsum - Summaa tiedoston numerot yhteen"
		+ "\n\tavg - Antaa tiedoston numeroiden keskiarvon"
		+ "\n\tmedian - Antaa tiedoston numeroiden mediaanin")
messageSource = ("Anna numeroita sisältävän tekstitiedoston nimi.")
warningSource = ("Tarkista numeroita sisältävän tekstitiedoston nimi.")
messageComparison = ("Anna vertailuoperaatio:"
		+ "\n\tgt - Onko annettu numero suurempi kuin tulos?"
		+ "\n\tlt - Onko annettu numero pienempi kuin tulos?"
		+ "\n\teq - Onko annettu numero samanarvoinen kuin tulos?")
warningMax = ("Voit antaa laskurille maksimissaan neljä parametriä.")
result = 0
numbers = []
if(len(sys.argv)<2):
	print(messageSource)
	exit()
if os.path.exists(sys.argv[1]):
	source = sys.argv[1]
else:
	print(warningSource)
	exit()
if(len(sys.argv)<3):
	print(messageOperation)
	exit()
with open(source) as data:
	for line in data:
		if(line != '\n'):
			numbers.append(int(line))
def sum():
	global numbers
	global result
	for number in numbers:
		result += number
	print('Summa on: ' + str(result))
def avg():
	global numbers
	totalsum=0
	divider=len(numbers)
	for number in numbers:
		totalsum = totalsum+number
	global result
	result=totalsum/divider
	print('Keskiarvo on: ' + str(result))
def median():
	global numbers
	sortedList = sorted(numbers)
	global result
	if((len(sortedList)%2)==1):
		i = (len(sortedList))//2
		result = str(sortedList[i])
		print('Mediaani on :' + result)
	else:
		i = (len(sortedList))//2
		j = i-1
		result = (sortedList[i]+sortedList[j])/2
		print("Mediaani on: " + str(result))
if (sys.argv[2] == 'sum'):
	sum()
elif (sys.argv[2] == 'avg'):
	avg()
elif (sys.argv[2] == 'median'):
	median()
else:
	print(messageOperation)
if (len(sys.argv)==4):
	print("Anna vertailumuuttuja (gt/lt/eq) ja numeerinen arvo, johon verrata.")
if (len(sys.argv)==5):
	result=float(result)
	compare = sys.argv[3]
	try:
		value = float(sys.argv[4])
	except ValueError:
		print("Tarkista vertailtava numero!")
		exit()
	if (compare == "gt"):
		if (result>value):
			print(str(result) + " on suurempi kuin " + str(value))
		else:
			print(str(result) + " ei ole suurempi kuin " + str(value))
	if (compare == "lt"):
		if (result<value):
			print(str(result) + " on pienempi kuin " + str(value))
		else:
			print(str(result) + " ei ole pienempi kuin " + str(value))
	if (compare == "eq"):
		if (result==value):
			print(str(result) + " on yhtä suuri kuin " + str(value))
		else:
			print(str(result) + " ei ole yhtä suuri kuin " + str(value))
if (len(sys.argv)>5):
	print(warningMax)