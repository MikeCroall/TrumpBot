# TrumpBot
## A chat bot to emulate Donald Trump's speech

### Download the App (Android 4.3+)
The Android app is now available on the play store! You can find it [here](https://play.google.com/store/apps/details?id=co.brookesoftware.mike.trumpbot) or by searching for TrumpBot.
#### NOTE: Currently broken while the server is moving hosting

### Goals
+ API that receives a string, returns a string response in the style of Donald Trump
  * /response will return a Trump style statement. - Done
  * /response?q=Query will return Trump's thoughts on your Query - Done
+ Automatically determine Donald Trump's style via tweet analysis (TensorFlow) - Not quite... see below
+ Text message wrapper for API calls (Twilio) - Done
+ Web wrapper for API calls - Done
+ Android App wrapper for API calls (eventually...) - Done

#### API Functionality
+ Train Neural Network
+ getResponse : input string -> output string

### Problems We Encountered
+ Tensorflow didn't seem to work, so after many hours of attempted (and failed) bug fixes, we switched from LSTM networks to simple Markov Chains.
+ Twitter has a limit on the number of tweets you can download. An alternative method of harvesting tweets was found.

### Dependencies
+ Python 3.5.2
+ Flask Python Package
+ Twython Python Package
+ h5py Python Package
+ scipy Python Package
+ Ngrok (temporary, for tunelling local server to the internet)
+ OhmGeek's fork of markov-sentence-generator (for generating the sentences)

### Running the bot
On Linux, simply open terminal, navigate to the folder where `run.sh` is located
```
$ cd /path/to/server/
```
Make sure run.sh is executable (note: this requires root)
```
$ chmod +x run.sh
```
Finally, run the script    
```
$ ./run.sh
```

### Twilio
To use Twilio, you will need to create an account, and go through all the Twilio sign up procedure (including gettting a phone number).

Once you have done this, go to the phone.py script and enter the URI of the main bot server.

```
$ python3 phone.py
```
This will run the phone server. Then enter the URI of the phone server in the section called 'Web Hooks' on Twilio.
