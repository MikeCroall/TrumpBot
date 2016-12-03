from flask import Flask, request, redirect, url_for
from trumpGen import TrumpGenerator
import re
import random
import sys
import string

app = Flask(__name__)
tg = None
stopList = ['a','an','and','are','as','at','be','by','for','from','has','he','in','is','it','its','of','on','that','the','to','was','were','will','with']

def run_on_start():
	global tg
	tg = TrumpGenerator(4)	
	tg.train("tweets.txt")

@app.route('/')
def root():
	return "API Working"

@app.route('/response', methods=['GET','POST'])
def getResponse():
	if(request.args.get('q') != None):
		return tg.getResponse(processInput(request.args.get('q')))
	else:
		#generate random trump sentence statically
		return tg.getResponse()

def processInput(inputStr):
	#strip punctuation
	inputStr.translate(string.punctuation)
	#remove stop words
	for w in stopList:
		inputStr.replace(w,"")

	#remove excess spaces
	re.sub('\s+',' ', inputStr).strip() #hehe
	#pick a random word
	startWord = random.choice(inputStr.split(" "))
	if(startWord is None):
		return "Wall"
	return startWord

if __name__ == '__main__':
	run_on_start()
	app.run(host='0.0.0.0', port=3000)
