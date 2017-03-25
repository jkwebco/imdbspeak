import omdb
import json
import pyttsx


import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 150)

variable = ""
while variable != 'quit':

	variable = raw_input('Lookup a movie, type something in: ')
	res = omdb.request(t=variable)
	xml_content = res.content

	parsed_json = json.loads(xml_content)

	test = (parsed_json['Plot'])	
	print (test)

	engine.say('The plot of this movie is. .')

	engine.say(test)
	engine.runAndWait()



