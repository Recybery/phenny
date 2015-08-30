from subprocess import call, check_output
def boincStatus(phenny, input):
	phial = open("/home/recybery/boincStatus.out","r")
	lines = phial.readlines()
	phial.close()
	for line in lines:
		phenny.say(line)
	phenny.say(''.join(lines))
boincStatus.commands = ['boinc']
boincStatus.priority = 'medium'
