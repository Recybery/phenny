import string
import os
from datetime import datetime
from time import sleep

def tail(f, n):
	stdin,stdout = os.popen2("tail -n "+str(n)+" "+f)
	stdin.close()
	lines = stdout.readlines(); stdout.close()
	return lines


  
def fillMeIn(phenny, input):
	try:
		nLines=max(250, int(input.group(2)))
	except TypeError:
		nLines = 25
	history=tail('%s_%s_irc.log'%tuple([datetime.utcnow().month, datetime.utcnow().year]), nLines)
	for line in history:
		phenny.msg(input.nick, line) 
		sleep(0.1)
	
	

fillMeIn.commands = ['fillMeIn']
fillMeIn.priority= 'medium'
