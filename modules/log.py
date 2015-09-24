"""
log.py - Phenny Log Module
Copyright (c) Esteban Feldman

BSD License

http://github.com/eka/
"""

from datetime import datetime
import os


def f_log(phenny, input):
	phial = open('%s_%s_irc.log'%tuple([datetime.utcnow().month, datetime.utcnow().year]), 'a')
#	print '%s - %s - %s: %s' % (datetime.utcnow().strftime('%m-%d-%Y %H:%M:%S'), input.sender, input.nick, input)	
	phial.write( '%s - %s - %s: %s\n' % (datetime.utcnow().strftime('%m-%d-%Y %H:%M:%S'), input.sender, input.nick, input))
	phial.close()
f_log.rule = r'(.+)'
f_log.priority = 'high'
f_log.thread = False
