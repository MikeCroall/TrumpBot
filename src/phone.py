from flask import Flask, request, redirect
import twilio.twiml
import requests
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def respondToPerson():
	fromContact = request.values.get('From',None);
	inputMessage = request.values.get('Body',None);
	param = {'q':inputMessage}
	#get a response from the Trump API
	res = requests.get('http://32d4b85d.ngrok.io/response',param)

	#send info to the person
	resp = twilio.twiml.Response()
	resp.message(res.text)

	return str(resp)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port="5000")
