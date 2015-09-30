#!/usr/bin/python

import urllib2

url = 'http://www.team-cymru.org/Services/Bogons/fullbogons-ipv4.txt'

obj = urllib2.urlopen(url)


for x in obj:
	print ('ip access-list bogon ' + x)
	
