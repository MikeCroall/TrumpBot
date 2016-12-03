from flask import Flask, request, redirect, url_for
from trumpGen import TrumpGenerator

app = Flask(__name__)

@app.route('/')
def root():
	return "API Working"

@app.route('/response')
def getResponse():
	if(request.args['q']):
		//use TF on model
	else:
		//generate random trump sentence statically



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000)

