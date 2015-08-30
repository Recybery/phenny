import string
D= {}
#'''
#'''

D["a"]=".-"
D["b"]="-..."
D["c"]="-.-."
D["d"]="-.."
D["e"]="."
D["f"]="..-."
D["g"]="--."
D["h"]="...."
D["i"]=".."
D["j"]=".---"
D["k"]="-.-"
D["l"]=".-.."
D["m"]="--"
D["n"]="-."
D["o"]="---"
D["p"]=".--."
D["q"]="--.-"
D["r"]=".-."
D["s"]="..."
D["t"]="-"
D["u"]="..-"
D["v"]="...-"
D["w"]=".--"
D["x"]="-..-"
D["y"]="-.--"
D["z"]="--.."
D[" "]=""
D['1']=".----"
D['2']="..---"
D['3']="...--"
D['4']="....-"
D['5']="....."
D['6']="-...."
D['7']="--..."
D['8']="---.."
D['9']="----."
D['0']="-----"
D['.']=".-.-.-"
D[',']="--..--"
D['?']="..--.."
D['/']="-..-."
D['@']=".--.-."
D[':']="---..."
D['-']="-....-"
D['\'' ]=".----."#apostrophe
D['/']="-..-."
D['$']="...-..-"
D['"']=".-..-."
D[';']="-.-.-."
D['=']="-...-"


def TextToMorse(a):
	a=string.lower(a)
	B=""
	for i in  range(0,len(a)):
		B+=D[a[i]]+"/"
		
	return B
def getKey(a):
	for i in D.keys():
		if D[i]==str(a):
			return i
	return -1
			
def MorseToText(a):
	B=""
	try:
		F=a.split("/")
	except AttributeError:
		pass	
	for i in F:
		c= getKey(i)
		if c!=-1:
				B+=c
	return B

def morser(phenny, input):
	phenny.say(TextToMorse(input.group(2)))
morser.commands = ['2morse']
morser.priority = 'medium'

def morse(phenny, input):
	phenny.say(MorseToText(input.group(2)))
morse.commands = ['2text']
morse.priority= 'medium'