#!/usr/bin/env python

import random
import os
import sys

animals    = ['manatee',  'dugong',  'stellarsseacow','arrowroot','beet','burdock','camas','carrot','cassava','cattail','celery','daikon','garlic','ginger','ginsing','horseradish','jimica','lotus','onion','parsley','parsnip','peanut','potato','radish','rutabaga','shallot','taro','turnip','yam','rootytooty','tuber','tomato']

def makeanimaldockerfile(animal, password, httpport, sshport):
	f = open('Dockerfile','r')
	filedata = f.read()
	f.close()
	
	newdata = filedata.replace("ANIMAL", animal)
	newdata = newdata.replace("PASSWORD", password)
	newdata = newdata.replace("HTTPPORT", str(httpport))
	newdata = newdata.replace("SSHPORT", str(sshport))

	try:
		os.makedirs(animal)
	except OSError:
		pass
	
	f = open(animal+'/Dockerfile','w')
	f.write(newdata)


#try :
#	print 'makeanimaldockerfile(\'manatee\', \'password\')'
#	makeanimaldockerfile('manatee', 'password')
#except :
#	print 'makeanimaldockerfile failed'


def addcontainertocompose(animal, password, httpport, sshport):
	f = open('compose-template.yml', 'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace("animal", animal)
	newdata = newdata.replace("password", password)
	newdata = newdata.replace("httpport", str(httpport))
	newdata = newdata.replace("sshport", str(sshport))

	f = open('docker-compose.yml', 'a+')
	f.write(newdata)

#try :
#	print 'make a compose.yml file'
#
#	compose = open('compose.yml', 'w')
#	compose.write('# pono@osuosl.org\n')
#	compose.close()
#
#	addcontainertocompose('seacow', 8888, 2222)
#	print 'addcontainertocompose(\'seacow\', 8888, 2222)'
#except :
#	print 'addcontainertocompose failed'


def make_containers(n):

	animals    = ['manatee',  'dugong',  'stellarsseacow','arrowroot','beet','burdock','camas','carrot','cassava','cattail','celery','daikon','garlic','ginger','ginsing','horseradish','jimica','lotus','onion','parsley','parsnip','peanut','potato','radish','rutabaga','shallot','taro','turnip','yam','rootytooty','tuber','tomato']
	passwords  = [0]*n
	ssh_ports = random.sample(range(2200,2299), n)
	http_ports  = random.sample(range(8000,8099), n)

	compose = open('docker-compose.yml', 'w')
	compose.write('# pono@osuosl.org\n')
	compose.close()

	for i in range(0,n):
		passwords[i] = animals[i]+str(random.randint(100000,999999))
		makeanimaldockerfile(animals[i], passwords[i], http_ports[i], ssh_ports[i])
		addcontainertocompose(animals[i], passwords[i], http_ports[i], ssh_ports[i])


#make_containers(len(animals))

#try :
#	make_containers(3)
#	print 'make_containers(3)'
#
#except :
#	print 'make_containers failed'

numberofcontainers = sys.argv[1]

try:
	if numberofcontainers == "all":
		numberofcontainers = len(animals)
	else:
		numberofcontainers = int(numberofcontainers)
	
	make_containers(numberofcontainers)

except:
	print "Whoops, try a (smaller) number"

