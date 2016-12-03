from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def respondToPerson():
	fromContact = request.values.get('From',None);
	inputMessage = request.values.get('Body',None);	
	#get a response from the Trump API


	#send info to the person
	resp = twilio.twiml.Response()
	resp.message(inputMessage)

	return str(resp)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port="5000")
